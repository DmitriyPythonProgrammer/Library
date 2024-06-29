from repositories.authors import AuthorRepository
from repositories.books import BookRepository
from services.authors import AuthorService
from services.books import BookService
from utils.database import async_session

# repository - работа с БД
book_repository = BookRepository()

author_repository = AuthorRepository()

# service - слой UseCase
book_service = BookService(book_repository)

author_service = AuthorService(author_repository)


def get_book_service() -> BookService:
    yield book_service


def get_author_service() -> AuthorService:
    yield author_service


async def get_db():
    async with async_session() as session:
        async with session.begin():
            yield session
