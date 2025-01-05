from sqlalchemy import Column, String
from app.db.base import Base


class User(Base):
    email = Column(String(length=128), unique=True, index=True)
    name = Column(String(length=128), nullable=True)
    password = Column(String(length=64))
