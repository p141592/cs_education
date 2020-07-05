import sqlalchemy as s

from core.db import BaseDBModel


class Schedule(BaseDBModel):
    calendar_url = s.Column(s.String)
    calendar_id = s.Column(s.String)


class Slot(BaseDBModel):
    start = s.Column(s.DateTime)
    end = s.Column(s.DateTime)
    schedule_id = s.Column(s.Integer, s.ForeignKey("schedule.id"))
