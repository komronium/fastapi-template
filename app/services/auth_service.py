from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from pydantic import EmailStr
from app.core.security import hash_password, create_access_token, verify_password
from app.models.user import User
from app.schemas.auth import LoginRequest, SignupRequest


class AuthService:

    @staticmethod
    def authenticate(db: Session, email: EmailStr, password: str):
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.password):
            return None
        return user

    @staticmethod
    def login(db: Session, login_request: LoginRequest):
        user = AuthService.authenticate(db, login_request.email, login_request.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid credentials',
                headers={'WWW-Authenticate': 'Bearer'},
            )

        access_token = create_access_token({'sub': user.email})
        return {'access_token': access_token, 'token_type': 'bearer'}

    @staticmethod
    def signup(db: Session, signup_request: SignupRequest):
        existing_user = db.query(User).filter(User.email == signup_request.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Email already exists'
            )

        hashed_password = hash_password(signup_request.password)
        user = User(
            email=signup_request.email,
            password=hashed_password,
            name=signup_request.name
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
