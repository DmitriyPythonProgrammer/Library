from typing import Sequence

from sqlalchemy.orm import Session

from models.book import Book
from repositories.books import BookRepository
from schemas.books import BookSchemaIn, BookSchemaOut


class BookService:

    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    async def get_books(self, db: Session) -> Sequence[Book]:
        result = await self.repository.get_books(db)
        return result

    async def create_book(self, book: BookSchemaIn, db: Session) -> BookSchemaOut:
        book = await self.repository.create_book(Book(**book.model_dump()), db)
        result = BookSchemaOut(**book.__dict__)
        return result

    async def get_book(self, book_id: int, db: Session) -> BookSchemaOut | None:
        if (await self.repository.exists_book(book_id, db)):
            book = await self.repository.get_book(book_id, db)
            result = BookSchemaOut(**book.__dict__)
        else:
            result = None
        return result

    async def delete_book(self, book_id: int, db: Session) -> None:
        await self.repository.delete_book(book_id, db)
