from pydantic import BaseModel
import datetime


class Users(BaseModel):
    id: int
    id_user: int
    answer: str
    question: str
    datetime: datetime.datetime
