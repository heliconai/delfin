from typing import Any

from sqlalchemy import TIMESTAMP, Column
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql import func


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    @declared_attr
    def created_on(cls) -> TIMESTAMP:
        return Column(TIMESTAMP(timezone=True), default=func.now(), nullable=False)

    @declared_attr
    def updated_on(cls) -> TIMESTAMP:
        return Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())
