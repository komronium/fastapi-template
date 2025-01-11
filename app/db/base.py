import re
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=True)

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Converts CamelCase class names to snake_case table names.
        For example, 'MyModel' becomes 'my_model'.
        """
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__)
        return name.lower()
