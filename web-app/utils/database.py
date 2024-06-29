from config import SQLALCHEMY_DATABASE_URL
from models.author import Author
from models.book import Book
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    poolclass=NullPool
)

async_session = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Author.metadata.create_all)
        await conn.run_sync(Book.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Author.metadata.drop_all)
        await conn.run_sync(Book.metadata.drop_all)
