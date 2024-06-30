from aiogram.fsm.state import StatesGroup, State


class LibraryStates(StatesGroup):
    book_name = State()
    author_name = State()
