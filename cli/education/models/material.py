import sqlalchemy as s

from core.db import BaseDBModel, BaseDBHandbook


class MaterialType(BaseDBHandbook):
    pass


class ContentType(BaseDBHandbook):
    pass


class Section(BaseDBHandbook):
    pass


class Topic(BaseDBHandbook):
    parent_id = s.Column(s.Integer, s.ForeignKey("topic.id"))


class Resource(BaseDBModel):
    readable_field = "title"

    title = s.Column(s.String)
    url = s.Column(s.String)
    section_id = s.Column(s.Integer, s.ForeignKey("section.id"))
    content_type_id = s.Column(s.Integer, s.ForeignKey("contenttype.id"))


class Material(BaseDBModel):
    readable_field = "title"

    title = s.Column(s.Text)
    brief = s.Column(s.Text)
    minute_estimate = s.Column(s.Integer)

    parent_id = s.Column(s.Integer, s.ForeignKey("material.id"))
    topic_id = s.Column(s.Integer, s.ForeignKey("topic.id"))
    material_type_id = s.Column(s.Integer, s.ForeignKey("materialtype.id"))
    resource_id = s.Column(s.Integer, s.ForeignKey("resource.id"))
