from aiogram.types import Message

from utils.create_bot import dp


@dp.message()
async def echo(message: Message) -> None:
    await message.answer(message.text)
