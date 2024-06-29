from datetime import date
from pydantic import BaseModel


class AuthorSchemaIn(BaseModel):
    first_name: str
    last_name: str
    date_birth: date
    biography: str


class AuthorSchemaOut(AuthorSchemaIn):
    id: int