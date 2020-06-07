import sqlalchemy as s
from sqlalchemy.ext.declarative import declared_attr

from core import Base


class BaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = s.Column(s.Integer, primary_key=True, unique=True, autoincrement=True)
