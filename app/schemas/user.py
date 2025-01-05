from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    name: str | None = None


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(UserBase):
    email: EmailStr | None = None


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
