from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, HttpUrl


class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)


class UserUpdate(BaseModel):
    name: Optional[str] = None


class UserOut(UserBase):
    id: int
    profile_image: Optional[HttpUrl]
    last_login: Optional[datetime]

    is_active: bool
    is_admin: bool

    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
