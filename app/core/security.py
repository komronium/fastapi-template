from typing import Optional, Dict
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt, JWTError

from app.core.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    payload = data.copy()
    expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({'exp': expire})
    
    return jwt.encode(
        payload,
        settings.SECRET_KEY.get_secret_value(),
        algorithm=settings.ALGORITHM
    )


def decode_access_token(token: str) -> Optional[Dict]:
    try:
        return jwt.decode(
            token,
            settings.SECRET_KEY.get_secret_value(),
            algorithms=[settings.ALGORITHM]
        )
    except JWTError:
        return None
