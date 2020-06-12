from pydantic import BaseModel


class BaseHandbook(BaseModel):
    id: int
    title: str
