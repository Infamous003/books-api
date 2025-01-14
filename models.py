from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Integer, String

class Book(SQLModel, table = True):
  id: int = Field(primary_key=True, nullable=False)
  title: str = Field(String(128), nullable=False, unique=True)
  author: str = Field(String(64), nullable=False)
  pages: int | None = Field(default=None)

class BookCreate(BaseModel):
  title: str
  author: str
  pages: int | None = None