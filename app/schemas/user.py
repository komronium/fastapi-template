from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)


class UserUpdate(BaseModel):
    name: Optional[str] = None


class UserOut(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    last_login: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
