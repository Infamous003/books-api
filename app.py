from fastapi import FastAPI, HTTPException, status
from models import Book, BookCreate, BookUpdate
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
  with Session(db) as session:
    statement = select(Book).where(Book.id == id)
    bookExists = session.exec(statement).one_or_none()

    if not bookExists:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return bookExists

@app.post("/books")
def create_books(book: BookCreate) -> Book:
  with Session(db) as session:
    statement = select(Book).where(Book.title == book.title)
    bookExists = session.exec(statement).one_or_none()

    if bookExists:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book already exists")
    
    new_book = Book(**book.model_dump())
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book


@app.put("/books/{id}")
def update_books(id: int, book: BookUpdate) -> Book:
  with Session(db) as session:
    statement = select(Book).where(Book.id == id)
    bookExists = session.exec(statement).one_or_none()

  if not bookExists:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

  # if book.title: bookExists.title = book.title
  # if book.author: bookExists.author = book.author

  # Creating a dictionary of only the data that has been provided in req body
  # exclude fields that have not been explicitly set
  update_data = book.model_dump(exclude_unset=True)

  for key, value in update_data.items():
    setattr(bookExists, key, value)


  session.add(bookExists)
  session.commit()
  session.refresh(bookExists)
  return bookExists

@app.delete("/books/{id}")
def delete_books(id: int):
  with Session(db) as session:
    statement = select(Book).where(Book.id == id)
    bookExists = session.exec(statement).one_or_none()

  if not bookExists:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

  session.delete(bookExists)
  session.commit()
