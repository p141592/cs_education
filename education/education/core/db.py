import orjson
import sqlalchemy as s
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class BaseDBModel(Base):
    __abstract__ = True
    Serializer = None

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = s.Column(s.Integer, primary_key=True, unique=True, autoincrement=True)


class BaseSerializerModel(BaseModel):
    pass

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        orm_mode = True
