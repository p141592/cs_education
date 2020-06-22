import sqlalchemy as s

from core.db import BaseDBModel, BaseSerializerModel


class BaseHandbook(BaseSerializerModel):
    id: int = None
    title: str
    key: str = None


class BaseDBHandbook(BaseDBModel):
    __abstract__ = True

    title = s.Column(s.String)
    key = s.Column(s.String)

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.title}>'


class Section(BaseDBHandbook):
    pass

    class Serializer(BaseHandbook):
        pass


class MaterialType(BaseDBHandbook):
    pass

    class Serializer(BaseHandbook):
        pass


class ContentType(BaseDBHandbook):
    pass

    class Serializer(BaseHandbook):
        pass


class Tag(BaseDBHandbook):
    pass

    class Serializer(BaseHandbook):
        pass


class LessonType(BaseDBHandbook):
    pass

    class Serializer(BaseHandbook):
        pass


class QuizType(BaseDBHandbook):
    pass

    class Serializer(BaseHandbook):
        pass
