from sqlalchemy import Column, String, Boolean, DateTime
from app.db.base import Base


class User(Base):
    email = Column(String(length=128), unique=True, index=True, nullable=False)
    name = Column(String(length=128), nullable=True)
    password = Column(String(length=64), nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    last_login = Column(DateTime(timezone=True), nullable=True)
