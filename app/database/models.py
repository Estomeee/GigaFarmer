from typing import Any

from sqlalchemy import Column, String, DateTime, Integer, BigInteger
from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(BigInteger)
    answer = Column(String)
    question = Column(String)
    datatime = Column(DateTime)

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        if "users" in kwargs:
            users = kwargs["users"]
            self.id = users.id
            self.id_user = users.id
            self.questions = users.questions
            self.answers = users.answers
