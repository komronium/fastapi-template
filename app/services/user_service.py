from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate


class UserService:

    @staticmethod
    async def get_all_users(db: Session):
        return db.query(User).all()


    @staticmethod
    async def create_user(user_data: UserCreate, db: Session):
        existing_user = db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise HTTPException(detail='Email already exists', status_code=status.HTTP_400_BAD_REQUEST)

        hashed_password = hash_password(user_data.password)
        user_data.password = hashed_password
        db_user = User(**user_data.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    async def get_user_by_id(user_id: int, db: Session):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(detail='User not found', status_code=status.HTTP_404_NOT_FOUND)

        return user
