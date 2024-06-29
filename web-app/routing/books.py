from typing import Sequence
from fastapi import HTTPException, Security
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from depends import get_db
from depends import get_book_service
from models.book import Book
from schemas.books import BookSchemaIn, BookSchemaOut
from services.books import BookService
from utils.api_key import get_api_key

router = APIRouter(prefix="/books", tags=["books"])


@router.get(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=None,
    description="Получение листинга всех книг",
)
async def get_all_books(
        book_service: BookService = Depends(get_book_service),
        db: Session = Depends(get_db),
        api_key: str = Security(get_api_key)
) -> Sequence[Book]:
    books = await book_service.get_books(db)
    return books


@router.post(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=BookSchemaOut,
    description="Создание книги",
)
async def create_book(
        book: BookSchemaIn,
        book_service: BookService = Depends(get_book_service),
        db: Session = Depends(get_db),
        api_key: str = Security(get_api_key)
) -> BookSchemaOut:
    book = await book_service.create_book(book, db)
    return book


@router.get(
    "/{book_id}",
    responses={400: {"description": "Bad request"}},
    response_model=BookSchemaOut,
    description="Найти книгу",
)
async def get_book_by_id(
        book_id: int,
        book_service: BookService = Depends(get_book_service),
        db: Session = Depends(get_db),
        api_key: str = Security(get_api_key)
) -> BookSchemaOut:
    book = await book_service.get_book(book_id, db)
    if not book:
        raise HTTPException(status_code=404, detail="Object was not found")
    return book


@router.delete(
    "/{book_id}",
    responses={400: {"description": "Bad request"}},
    response_model=BookSchemaOut,
    description="Удаление книги",
)
async def delete_book(
        book_id: int,
        book_service: BookService = Depends(get_book_service),
        db: Session = Depends(get_db),
        api_key: str = Security(get_api_key)
) -> BookSchemaOut:
    book = await book_service.get_book(book_id, db)
    if not book:
        raise HTTPException(status_code=404, detail="Object was not found")
    await book_service.delete_book(book_id, db)
    return book


