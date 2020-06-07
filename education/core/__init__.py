import sqlalchemy as s

from sqlalchemy.ext.declarative import declarative_base

DB_PATH = 'sqlite:///knowledge_base.db'

Base = declarative_base()
