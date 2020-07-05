import sqlalchemy as s

from core.db import BaseDBHandbook, BaseDBModel


class Course(BaseDBHandbook):
    schedule_id = s.Column(s.Integer, s.ForeignKey("schedule.id"))


class Sequence(BaseDBModel):
    order = s.Column(s.Integer)
    topic_id = s.Column(s.Integer, s.ForeignKey("topic.id"))
    course_id = s.Column(s.Integer, s.ForeignKey("course.id"))
