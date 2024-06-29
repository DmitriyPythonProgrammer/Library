from typing import Sequence

from sqlalchemy.orm import Session

from models.author import Author
from repositories.authors import AuthorRepository
from schemas.authors import AuthorSchemaIn, AuthorSchemaOut


class AuthorService:

    def __init__(self, repository: AuthorRepository) -> None:
        self.repository = repository

    async def get_authors(self, db: Session) -> Sequence[Author]:
        result = await self.repository.get_authors(db)
        return result

    async def create_author(self, author: AuthorSchemaIn, db: Session) -> AuthorSchemaOut:
        author = await self.repository.create_author(Author(**author.model_dump()), db)
        result = AuthorSchemaOut(**author.__dict__)
        return result

    async def get_author(self, author_id: int, db: Session) -> AuthorSchemaOut | None:
        if (await self.repository.exists_author(author_id, db)):
            author = await self.repository.get_author(author_id, db)
            result = AuthorSchemaOut(**author.__dict__)
        else:
            result = None
        return result

    async def delete_author(self, author_id: int, db: Session) -> None:
        await self.repository.delete_author(author_id, db)
