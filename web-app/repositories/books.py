from typing import Sequence
from sqlalchemy import select, exists
from sqlalchemy.orm import Session
from models.book import Book


class BookRepository:

    @staticmethod
    async def get_books(db: Session) -> Sequence[Book]:
        request = (
            select(Book)
        )
        result = await db.execute(request)
        return result.scalars().all()

    @staticmethod
    async def create_book(book: Book, db: Session) -> Book:
        db.add(book)
        await db.flush()
        return book

    @staticmethod
    async def get_book(book_id: int, db: Session) -> Book:
        request = (
            select(Book)
            .where(Book.id == book_id)
        )
        result = await db.execute(request)
        return result.scalar_one()

    @staticmethod
    async def delete_book(book_id: int, db: Session) -> None:
        request = (
            select(Book)
            .where(Book.id == book_id)
        )
        row = await db.execute(request)
        row = row.scalar_one()
        await db.delete(row)

    @staticmethod
    async def exists_book(book_id: int, db: Session) -> bool:
        request = (
            exists(Book.id)
            .where(Book.id == book_id)
            .select()
        )
        result = await db.execute(request)
        return result.scalars().first()
