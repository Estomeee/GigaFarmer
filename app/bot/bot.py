from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from app.database.db import engine, Base
from app.giga.giga import get_giga_retriever
from langchain.schema import SystemMessage
from app.config import TG_TOKEN
from app.database.utils import get_history, add_request

TOKEN = TG_TOKEN
dp = Dispatcher()
crc = get_giga_retriever()

chat_history = [
    SystemMessage(
        content="Ты эмпатичный бот-фермер, который помогает пользователю решить его проблемы с животновдством, а именно с разведением крупного рогатого скота. Ты не должен отвечат на вопросы, не связанные с животноводством. Очень важно, чтобы ты вел диалог только о коровах!"
    )
]


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!")
    await message.answer(f"Как поживают твои коровы?")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    history = await get_history(id_user=message.chat.id)

    question = message.text
    result = crc({"question": question, "chat_history": history})

    await add_request(
        id_user=message.chat.id, question=question, answer=result["answer"]
    )

    await message.answer(str(result["answer"]))


async def create_db():
    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await create_db()
    await dp.start_polling(bot)
