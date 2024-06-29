from typing import Sequence
from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from depends import get_db
from depends import get_author_service
from models.author import Author
from schemas.authors import AuthorSchemaIn, AuthorSchemaOut
from services.authors import AuthorService
from utils.api_key import get_api_key

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=None,
    description="Получение листинга всех авторов",
)
async def get_all_authors(
        author_service: AuthorService = Depends(get_author_service),
        db: Session = Depends(get_db),
        api_key: str = Security(get_api_key)
) -> Sequence[Author]:
    authors = await author_service.get_authors(db)
    return authors


@router.post(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=AuthorSchemaOut,
    description="Создание автора",
)
async def create_author(
        author: AuthorSchemaIn,
        author_service: AuthorService = Depends(get_author_service),
        db: Session = Depends(get_db),
        api_key: str = Security(get_api_key)
) -> AuthorSchemaOut:
    author = await author_service.create_author(author, db)
    return author


@router.get(
    "/{author_id}",
    responses={400: {"description": "Bad request"}},
    response_model=AuthorSchemaOut,
    description="Найти автора",
)
async def get_author_by_id(
        author_id: int,
        author_service: AuthorService = Depends(get_author_service),
        db: Session = Depends(get_db),
        api_key: str = Security(get_api_key)
) -> AuthorSchemaOut:
    author = await author_service.get_author(author_id, db)
    if not author:
        raise HTTPException(status_code=404, detail="Object was not found")
    return author


@router.delete(
    "/{author_id}",
    responses={400: {"description": "Bad request"}},
    response_model=AuthorSchemaOut,
    description="Удаление автора",
)
async def delete_author(
        author_id: int,
        author_service: AuthorService = Depends(get_author_service),
        db: Session = Depends(get_db),
        api_key: str = Security(get_api_key)
) -> AuthorSchemaOut:
    author = await author_service.get_author(author_id, db)
    if not author:
        raise HTTPException(status_code=404, detail="Object was not found")
    await author_service.delete_author(author_id, db)
    return author
