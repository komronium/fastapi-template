from pydantic import BaseModel, EmailStr, Field


class Token(BaseModel):
    access_token: str
    tekon_type: str = 'bearer'


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class SignupRequest(BaseModel):
    name: str | None = None
    email: EmailStr
    password: str = Field(..., min_length=8)
