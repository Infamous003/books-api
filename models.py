from pydantic import BaseModel
from sqlmodel import SQLModel, Field, String

class Book(SQLModel, table = True):
  id: int = Field(primary_key=True, nullable=False)
  title: str = Field(String(128), nullable=False, unique=True)
  author: str = Field(String(64), nullable=False)
  summary: str | None = Field(String(2046))
  publication_year: int | None = Field(default=None)
  genre: str | None = Field(default=None)
  pages: int | None = Field(default=None)
  language: str | None = Field(default="english")
  is_available: bool | None = Field(default=True)

class BookCreate(BaseModel):
  title: str
  author: str
  summary: str | None = None
  publication_year: int | None = None
  genre: str | None = None
  pages: int | None = None
  language: str | None = None
  is_available: bool | None = None

class BookUpdate(BaseModel):
  title: str | None = None
  author: str | None = None
  summary: str | None = None
  publication_year: int | None = None
  genre: str | None = None
  pages: int | None = None
  language: str | None = None
  is_available: bool | None = None