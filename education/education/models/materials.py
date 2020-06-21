from datetime import datetime

import sqlalchemy as s
from pydantic import BaseModel
from sqlalchemy import func

from core.db import BaseDBModel, BaseSerializerModel


class Material(BaseDBModel):
    section = s.Column(s.Integer, s.ForeignKey('section.id'))
    material_type = s.Column(s.Integer, s.ForeignKey('materialtype.id'))
    content_type = s.Column(s.Integer, s.ForeignKey('contenttype.id'))
    source = s.Column(s.String)
    volume = s.Column(s.Integer, doc="Объем материала в минутах")

    class Serializer(BaseModel):
        section: int
        material_type: int
        content_type: int
        source: str
        volume: int


class Resource(BaseDBModel):
    link = s.Column(s.String)
    description = s.Column(s.Text, nullable=True)

    class Serializer(BaseSerializerModel):
        link: str
        description: str

    @property
    def object(self):
        return self.Serializer.from_orm(self)


class Quiz(BaseDBModel):
    quiz_type = s.Column(s.Integer, s.ForeignKey('quiztype.id'))
    question = s.Column(s.String)
    answer = s.Column(s.String)
    material = s.Column(s.Integer, s.ForeignKey('material.id'))

    class Serializer(BaseSerializerModel):
        quiz_type: int
        question: str
        answer: str
        material: int


class QuizLog(BaseDBModel):
    quiz = s.Column(s.Integer, s.ForeignKey('quiz.id'))
    date = s.Column(s.DateTime, default=func.now())
    answer = s.Column(s.Text)
    result = s.Column(s.Boolean, default=False)

    class Serializer(BaseSerializerModel):
        quiz: int
        date: datetime
        answer: str
        result: bool


class Epic(BaseDBModel):
    title = s.Column(s.String)

    class Serializer(BaseSerializerModel):
        title: str


class Story(BaseDBModel):
    order = s.Column(s.Integer)
    epic = s.Column(s.Integer, s.ForeignKey('epic.id'))
    time_estimate = s.Column(s.Integer, doc="В минутах")
    story_points = s.Column(s.Integer, doc="Оценка сложности")
    start_date = s.Column(s.DateTime, default=func.now())
    end_date = s.Column(s.DateTime, nullable=True)
    material = s.Column(s.Integer, s.ForeignKey('material.id'))

    class Serializer(BaseSerializerModel):
        order: int
        epic: int
        time_estimate: int
        story_points: int
        start_date: datetime
        end_date: datetime
        material: int


class Lesson(BaseDBModel):
    title = s.Column(s.String)
    text = s.Column(s.Text)
    lesson_type = s.Column(s.Integer, s.ForeignKey('lessontype.id'))

    class Serializer(BaseSerializerModel):
        title: str
        text: str
        lesson_type: int


class Note(BaseDBModel):
    lesson = s.Column(s.Integer, s.ForeignKey('lesson.id'))
    text = s.Column(s.Text)
    date = s.Column(s.DateTime, default=func.now())

    class Serializer(BaseSerializerModel):
        lesson: int
        text: str
        date: datetime


class Timer(BaseDBModel):
    start_date = s.Column(s.DateTime, nullable=True)
    end_date = s.Column(s.DateTime, default=func.now())
    text = s.Column(s.Text, nullable=True)
    lesson = s.Column(s.Integer, s.ForeignKey('lesson.id'))

    class Serializer(BaseSerializerModel):
        start_date: datetime
        end_date: datetime
        text: str
        lesson: int
