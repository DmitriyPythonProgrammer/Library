from datetime import date

from sqlalchemy import String, ForeignKey, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Book(Base):
    __tablename__ = "Book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(250))
    annotation: Mapped[str] = mapped_column(String(100))
    date_publishing: Mapped[date] = mapped_column(Date())
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("Author.id"))
    author: Mapped["Author"] = relationship(back_populates="books")

