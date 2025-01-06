import re
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(self) -> str:
        """
        Converts CamelCase class names to snake_case table names.
        For example, 'MyModel' becomes 'my_model'.
        """
        return re.sub(r'(?<!^)(?=[A-Z])', '_', self.__name__).lower()
