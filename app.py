from fastapi import FastAPI, HTTPException, status
from models import Book
from database import create_db_and_tables, db

app = FastAPI()
create_db_and_tables()


BOOKS = [
  {"id": 1, "title": "The Alchemist", "author": "Paulo Coehlo", "pages": 328},
  {"id": 2, "title": "The Digital Fortress", "author": "Dan Brown", "pages": 283},
  {"id": 3, "title": "Dracula", "author": "idmnam", "pages": 188},
  {"id": 2, "title": "Journey to the West", "author": "Chinese guy", "pages": 411}
]

@app.get("/")
def index():
  return {"Hello" : "World"}

@app.get("/books")
def get_books() -> list[Book]:
  return BOOKS

@app.get("/books/{id}")
def get_books(id: int) -> list[Book]:
  bookExists = [book for book in BOOKS if book.get("id") == id]

  if not bookExists:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
  return bookExists
