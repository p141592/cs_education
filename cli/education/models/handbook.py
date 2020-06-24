import sqlalchemy as s

from core.db import BaseDBModel


class BaseDBHandbook(BaseDBModel):
    __abstract__ = True
    readable_field = "title"

    title = s.Column(s.String)
    key = s.Column(s.String)


class Section(BaseDBHandbook):
    pass


class MaterialType(BaseDBHandbook):
    pass


class ContentType(BaseDBHandbook):
    pass


class Tag(BaseDBHandbook):
    pass


class LessonType(BaseDBHandbook):
    pass


class QuizType(BaseDBHandbook):
    pass
