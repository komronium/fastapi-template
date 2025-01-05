from sqlalchemy import Column, String
from app.db.base import Base


class User(Base):
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)
