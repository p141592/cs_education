from pydantic import BaseModel


class Material(BaseModel):
    section: int
    material_type: int
    content_type: int
    source: str
    volume: int


class Resource(BaseModel):
    link: str
    description: str


class Quiz(BaseModel):
    quiz_type: int
    question: str
    answer: str
    material: int


class QuizLog(BaseModel):
    quiz: int
    date = s.Column(s.DateTime, default=func.now())
    answer: str
    result: bool


class Epic(BaseModel):
    title: str


class Story(BaseModel):
    order: int
    epic: int
    time_estimate: int
    story_points: int
    start_date = s.Column(s.DateTime, default=func.now())
    end_date = s.Column(s.DateTime, nullable=True)
    material: int


class Lesson(BaseModel):
    title: str
    text: str
    lesson_type: int


class Note(BaseModel):
    lesson: int
    text: str
    date = s.Column(s.DateTime, default=func.now())


class Timer(BaseModel):
    start_date = s.Column(s.DateTime, nullable=True)
    end_date = s.Column(s.DateTime, default=func.now())
    text: str
    lesson: int
