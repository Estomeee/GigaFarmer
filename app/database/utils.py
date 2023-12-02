from datetime import datetime

from sqlalchemy import select

from app.database.db import async_session_maker
from app.database.models import User


async def get_history(id_user: int, offset: int = 0):
    async with async_session_maker() as db_session:
        histories = await db_session.scalars(
            select(User)
            .where(User.id_user == id_user)
            .order_by(User.datatime)
            .offset(offset)
        )
        history_user = [(item.question, item.answer) for item in histories]

    return history_user


async def add_request(id_user: int, question: str, answer: str):
    async with async_session_maker() as db_session:
        user = User(
            id_user=id_user,
            question=question,
            answer=answer,
            datatime=datetime.utcnow(),
        )

        db_session.add(user)
        await db_session.commit()


# TODO обработка ошибок
