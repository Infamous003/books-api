from fastapi import FastAPI, HTTPException, status
from models import Book, BookCreate
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
def create_books(book: BookCreate):
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



def addBooks():
  with Session(db) as session:
    b1 = Book(title="ksgbjskd", author="okkok", pages=123)
    b2 = Book(title="ksgbjssdsdskd", author="fvokkok", pages=1323)
    b3 = Book(title="ksgbsddsjskd", author="okvfvkok", pages=1553)

    session.add_all([b1, b2, b3])
    session.commit()

# addBooks()
