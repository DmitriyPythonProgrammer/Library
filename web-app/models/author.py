from datetime import date
from typing import List

from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.base import Base


class Author(Base):
    __tablename__ = "Author"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    date_birth: Mapped[date] = mapped_column(Date())
    biography: Mapped[str] = mapped_column(String(200))
    books: Mapped[List["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")


