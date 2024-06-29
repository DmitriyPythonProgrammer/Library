from datetime import date
from pydantic import BaseModel


class BookSchemaIn(BaseModel):
    name: str
    title: str
    annotation: str
    date_publishing: date
    author_id: int


class BookSchemaOut(BookSchemaIn):
    id: int