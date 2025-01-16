import re
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class SignupRequest(BaseModel):
    name: Optional[str] = None
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

    @field_validator('password', mode='before')
    @classmethod
    def validate_password(cls, value: str):
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must include at least one uppercase letter')
        if not re.search(r'[a-z]', value):
            raise ValueError('Password must include at least one lowercase letter')
        if not re.search(r'\d', value):
            raise ValueError('Password must include at least one digit')
        if not re.search(r'[!@#$%^&*(),.?\':{}|<>]', value):
            raise ValueError('Password must include at least one special character')
        return value
