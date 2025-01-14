from fastapi import FastAPI, HTTPException, status
from models import Book
from database import create_db_and_tables, db
from sqlmodel import Session, select

app = FastAPI()
create_db_and_tables()

@app.get("/")
def index():
  return {"Hello" : "World"}

@app.get("/books")
def get_books() -> list[Book]:
  with Session(db) as session:
    statement = select(Book)
    books = session.exec(statement).fetchall()
    return books

@app.get("/books/{id}")
def get_books(id: int) -> Book:
  bookExists = [book for book in BOOKS if book.get("id") == id]

  with Session(db) as session:
    statement = select(Book).where(Book.id == id)
    bookExists = session.exec(statement).one_or_none()

    if not bookExists:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return bookExists


# @app.post("/books")
# def create_books(book: Book):
#   with(Session) as session:
#     statement = select(Book)

