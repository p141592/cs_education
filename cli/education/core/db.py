import orjson
import sqlalchemy as s
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.compat import contextmanager

DB_PATH = 'sqlite:///knowledge_base.db'

Base = declarative_base()
engine = create_engine(
    DB_PATH,
    echo=True,
    connect_args={"check_same_thread": False}
)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class BaseDBModel(Base):
    __abstract__ = True
    _model = None
    readable_field = 'id'

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = s.Column(s.Integer, primary_key=True, unique=True, autoincrement=True)

    @classmethod
    def model(cls):
        if not cls._model:
            cls._model = sqlalchemy_to_pydantic(cls)
        return cls._model

    def __repr__(self):
        return f'<{self.__class__.__name__}: {getattr(self, self.readable_field)}>'
