import re
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(self) -> str:
        return re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', self.__name__).lower()
