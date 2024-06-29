from typing import Sequence
from sqlalchemy import select, exists
from sqlalchemy.orm import Session

from models.author import Author


class AuthorRepository:

    @staticmethod
    async def get_authors(db: Session) -> Sequence[Author]:
        request = (
            select(Author)
        )
        result = await db.execute(request)
        return result.scalars().all()

    @staticmethod
    async def create_author(author: Author, db: Session) -> Author:
        db.add(author)
        await db.flush()
        return author

    @staticmethod
    async def get_author(author_id: int, db: Session) -> Author:
        request = (
            select(Author)
            .where(Author.id == author_id)
        )
        result = await db.execute(request)
        return result.scalar_one()

    @staticmethod
    async def delete_author(author_id: int, db: Session) -> None:
        request = (
            select(Author)
            .where(Author.id == author_id)
        )
        row = await db.execute(request)
        row = row.scalar_one()
        await db.delete(row)

    @staticmethod
    async def exists_author(author_id: int, db: Session) -> bool:
        request = (
            exists(Author.id)
            .where(Author.id == author_id)
            .select()
        )
        result = await db.execute(request)
        return result.scalars().first()
