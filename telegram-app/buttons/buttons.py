from aiogram import types

from .texts import all_books_txt, all_authors_txt, exists_book_txt, exists_author_txt

all_books_btn = types.KeyboardButton(text=all_books_txt)
all_authors_btn = types.KeyboardButton(text=all_authors_txt)
exists_book_btn = types.KeyboardButton(text=exists_book_txt)
exists_author_btn = types.KeyboardButton(text=exists_author_txt)
