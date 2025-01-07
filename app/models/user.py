from sqlalchemy import Column, String, Boolean, DateTime
from app.db.base import Base


class User(Base):
    email = Column(String(length=128), unique=True, index=True)
    name = Column(String(length=128), nullable=True)
    password = Column(String(length=64))

    profile_image = Column(String(length=256), nullable=True)
    last_login = Column(DateTime(timezone=True), nullable=True)

    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
