import sqlalchemy as s
from sqlalchemy import func

from core.db import BaseDBHandbook, BaseDBModel


class LessonType(BaseDBHandbook):
    description = s.Column(s.Text)
    goal = s.Column(s.Text)
    plan = s.Column(s.Text)
    result = s.Column(s.Text)


class Lesson(BaseDBModel):
    readable_field = "title"

    title = s.Column(s.String)
    story = s.Column(s.String)
    motivation = s.Column(s.String)

    lesson_type_id = s.Column(s.Integer, s.ForeignKey("lessontype.id"))
    parent_lesson_id = s.Column(s.Integer, s.ForeignKey("lesson.id"))


class LessonMaterialM2M(BaseDBModel):
    material_id = s.Column(s.Integer, s.ForeignKey("material.id"))
    lesson_id = s.Column(s.Integer, s.ForeignKey("lesson.id"))


class Note(BaseDBModel):
    text = s.Column(s.Text)
    date = s.Column(s.DateTime, default=func.now())
    lesson_id = s.Column(s.Integer, s.ForeignKey("lesson.id"))


class Timer(BaseDBModel):
    readable_field = "start"

    start = s.Column(s.DateTime, default=func.now())
    finish = s.Column(s.DateTime, nullable=True)
    lesson_id = s.Column(s.Integer, s.ForeignKey("lesson.id"))
