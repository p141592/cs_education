import sqlalchemy as s

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.compat import contextmanager
from typing import Container, Type
from pydantic import BaseConfig, BaseModel, create_model
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.properties import ColumnProperty


DB_PATH = "sqlite:///knowledge_base.db"

Base = declarative_base()
engine = create_engine(DB_PATH, echo=True, connect_args={"check_same_thread": False})


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = sessionmaker(bind=engine)()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class PydanticConfig(BaseConfig):
    orm_mode = True


def sqlalchemy_to_pydantic(db_model: Type, *, config: Type = PydanticConfig, exclude: Container[str] = []) -> Type[BaseModel]:
    mapper = inspect(db_model)
    fields = {}
    for attr in mapper.attrs:
        if isinstance(attr, ColumnProperty):
            if attr.columns:
                column = attr.columns[0]
                python_type = column.type.python_type
                name = attr.key
                if name in exclude:
                    continue
                default = None
                if column.default is None and not column.nullable:
                    default = ...
                fields[name] = (python_type, default)
    pydantic_model = create_model(
        db_model.__name__, __config__=config, **fields  # type: ignore
    )
    return pydantic_model


class BaseDBModel(Base):
    __abstract__ = True
    _model = None
    readable_field = "id"

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = s.Column(s.Integer, primary_key=True, unique=True, autoincrement=True)

    @classmethod
    def model(cls):
        if not cls._model:
            cls._model = sqlalchemy_to_pydantic(cls, config=PydanticConfig, exclude=["id"])
        return cls._model

    def __repr__(self):
        return f"<{self.__class__.__name__}: {getattr(self, self.readable_field)}>"
