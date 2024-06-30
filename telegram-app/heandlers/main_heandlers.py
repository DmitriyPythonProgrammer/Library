import aiohttp
from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from buttons.markups import start_mr
from buttons.texts import all_authors_txt, all_books_txt, exists_book_txt, exists_author_txt
from msgs.texts import start_text
from states.main import LibraryStates
from utils.create_bot import dp


@dp.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(start_text, reply_markup=start_mr)


@dp.message(F.text == all_authors_txt)
async def all_authors(message: Message) -> None:
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get("http://web:8000/authors") as resp:
            if resp.status == 200:
                authors = await resp.json()
                msg_text = "В данный момент доступны следующие авторы:\n"
                for i in authors:
                    msg_text += f"{i['id']}: {i['first_name']} {i['last_name']}\n"
            else:
                msg_text = f"Ошибка доступа к API, код {resp.status}"

    await message.answer(msg_text)


@dp.message(F.text == all_books_txt)
async def all_authors(message: Message) -> None:
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get("http://web:8000/books") as resp:
            if resp.status == 200:
                books = await resp.json()
                msg_text = "В данный момент доступны следующие книги:\n"
                for i in books:
                    msg_text += f"{i['id']}: {i['name']}\n"
            else:
                msg_text = f"Ошибка доступа к API, код {resp.status}"

    await message.answer(msg_text)


@dp.message(F.text == exists_book_txt)
async def exists_book(message: Message, state: FSMContext) -> None:
    await message.answer("Напишите айди")
    await state.set_state(LibraryStates.book_name)


@dp.message(F.text == exists_author_txt)
async def exists_author(message: Message, state: FSMContext) -> None:
    await message.answer("Напишите айди")
    await state.set_state(LibraryStates.author_name)


@dp.message(LibraryStates.author_name)
async def all_authors(message: Message, state: FSMContext) -> None:
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(f"http://web:8000/authors/{message.text}") as resp:
            if resp.status == 200:
                author = await resp.json()
                msg_text = "По вашему запросу найдены следующие авторы:\n"
                msg_text += f"{author['id']}: {author['first_name']} {author['last_name']}\n"
            else:
                msg_text = f"Мы ничего не нашли :("

    await message.answer(msg_text)
    await state.clear()


@dp.message(LibraryStates.book_name)
async def all_authors(message: Message, state: FSMContext) -> None:
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(f"http://web:8000/books/{message.text}") as resp:
            if resp.status == 200:
                book = await resp.json()
                msg_text = "По вашему запросу найдены следующие книги:\n"
                msg_text += f"{book['id']}: {book['name']}\n"
            else:
                msg_text = f"Мы ничего не нашли :("

    await message.answer(msg_text)
    await state.clear()
