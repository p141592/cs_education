import sqlalchemy as s
from sqlalchemy import func

from core.db import BaseModel


class Material(BaseModel):
    section = s.Column(s.Integer, s.ForeignKey('section.id'))
    material_type = s.Column(s.Integer, s.ForeignKey('materialtype.id'))
    content_type = s.Column(s.Integer, s.ForeignKey('contenttype.id'))
    source = s.Column(s.String)
    volume = s.Column(s.Integer, doc="Объем материала в минутах")


class Resource(BaseModel):
    link = s.Column(s.String)
    description = s.Column(s.Text, nullable=True)


class Quiz(BaseModel):
    quiz_type = s.Column(s.Integer, s.ForeignKey('quiztype.id'))
    question = s.Column(s.String)
    answer = s.Column(s.String)
    material = s.Column(s.Integer, s.ForeignKey('material.id'))


class QuizLog(BaseModel):
    quiz = s.Column(s.Integer, s.ForeignKey('quiz.id'))
    date = s.Column(s.DateTime, default=func.now())
    answer = s.Column(s.Text)
    result = s.Column(s.Boolean, default=False)


class Epic(BaseModel):
    title = s.Column(s.String)


class Story(BaseModel):
    order = s.Column(s.Integer)
    epic = s.Column(s.Integer, s.ForeignKey('epic.id'))
    time_estimate = s.Column(s.Integer, doc="В минутах")
    story_points = s.Column(s.Integer, doc="Оценка сложности")
    start_date = s.Column(s.DateTime, default=func.now())
    end_date = s.Column(s.DateTime, nullable=True)
    material = s.Column(s.Integer, s.ForeignKey('material.id'))


class Lesson(BaseModel):
    title = s.Column(s.String)
    text = s.Column(s.Text)
    lesson_type = s.Column(s.Integer, s.ForeignKey('lessontype.id'))


class Note(BaseModel):
    lesson = s.Column(s.Integer, s.ForeignKey('lesson.id'))
    text = s.Column(s.Text)
    date = s.Column(s.DateTime, default=func.now())


class Timer(BaseModel):
    start_date = s.Column(s.DateTime, nullable=True)
    end_date = s.Column(s.DateTime, default=func.now())
    text = s.Column(s.Text, nullable=True)
    lesson = s.Column(s.Integer, s.ForeignKey('lesson.id'))
