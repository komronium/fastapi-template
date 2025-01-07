from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile, status
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.storage_service import StorageService


class UserService:

    @staticmethod
    def _get_user_or_404(db: Session, user_id: int) -> User:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='User not found'
            )
        return user

    @staticmethod
    async def get_all_users(db: Session):
        return db.query(User).all()

    @staticmethod
    async def create_user(user_data: UserCreate, db: Session):
        existing_user = db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Email already exists'
            )

        hashed_password = hash_password(user_data.password)
        user_data.password = hashed_password
        db_user = User(**user_data.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    async def get_user_by_id(user_id: int, db: Session):
        return UserService._get_user_or_404(db, user_id)

    @staticmethod
    async def update_user(db: Session, user_id: int, user: UserUpdate):
        db_user = UserService._get_user_or_404(db, user_id)
        for key, value in user.model_dump().items():
            if value is not None:
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    async def update_profile_image(db: Session, user_id: int, file: UploadFile) -> User:
        user = UserService._get_user_or_404(db, user_id)
        try:
            if user.profile_image:
                await StorageService.delete_file(user.profile_image)

            image_url = await StorageService.upload_file(
                file=file,
                folder='profile_images'
            )

            user.profile_image = image_url
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Failed to update profile image'
            )

    @staticmethod
    async def remove_profile_image(db: Session, user_id: int) -> User:
        user = UserService._get_user_or_404(db, user_id)
        try:
            if user.profile_image:
                await StorageService.delete_file(user.profile_image)
                user.profile_image = None
                db.commit()
                db.refresh(user)
            return user
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to remove profile image"
            )

    @staticmethod
    async def delete_user(db: Session, user_id: int):
        db_user = UserService._get_user_or_404(db, user_id)
        db.delete(db_user)
        db.commit()
        return db_user
