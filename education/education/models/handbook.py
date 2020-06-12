# Описание вспомогательных моделей
import sqlalchemy as s

from core.db import BaseModel


class BaseHandbook(BaseModel):
    __abstract__ = True

    title = s.Column(s.String)
    key = s.Column(s.String)

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.title}>'


class Section(BaseHandbook): pass


class MaterialType(BaseHandbook): pass


class ContentType(BaseHandbook): pass


class Tag(BaseHandbook): pass


class LessonType(BaseHandbook): pass


class QuizType(BaseHandbook): pass
