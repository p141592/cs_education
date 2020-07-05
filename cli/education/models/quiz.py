import sqlalchemy as s
from sqlalchemy import func

from core.db import BaseDBModel, BaseDBHandbook


class QuizType(BaseDBHandbook):
    pass


class Quiz(BaseDBModel):
    readable_field = "question"

    question = s.Column(s.String)
    answer = s.Column(s.String)
    material_id = s.Column(s.Integer, s.ForeignKey("material.id"))
    quiz_type_id = s.Column(s.Integer, s.ForeignKey("quiztype.id"))


class QuizLog(BaseDBModel):
    start = s.Column(s.DateTime)
    finish = s.Column(s.DateTime)

    answer = s.Column(s.Text)
    date = s.Column(s.DateTime, default=func.now())
    quiz_id = s.Column(s.Integer, s.ForeignKey("quiz.id"))
