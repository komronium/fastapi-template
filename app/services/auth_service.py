from typing import Optional
from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from pydantic import EmailStr

from app.core.security import hash_password, create_access_token, verify_password
from app.models.user import User
from app.schemas.auth import LoginRequest, SignupRequest, Token


class AuthService:

    @staticmethod
    async def authenticate(db: Session, email: EmailStr, password: str) -> Optional[User]:
        user: Optional[User] = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.password):
            return None
        return user

    @staticmethod
    async def update_last_login(user: User, db: Session) -> None:
        user.last_login = datetime.now()
        db.commit()
        db.refresh(user)

    @staticmethod
    async def login(db: Session, request: LoginRequest) -> Token:
        user: Optional[User] = await AuthService.authenticate(db, request.email, request.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid credentials',
                headers={'WWW-Authenticate': 'Bearer'},
            )

        await AuthService.update_last_login(user, db)

        access_token = create_access_token({'sub': user.email})
        return Token(access_token=access_token)

    @staticmethod
    async def signup(db: Session, request: SignupRequest) -> User:
        existing_user: Optional[User] = db.query(User).filter(User.email == request.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Email already exists'
            )

        hashed_password = hash_password(request.password)
        user: User = User(
            email=request.email,
            password=hashed_password,
            name=request.name
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
