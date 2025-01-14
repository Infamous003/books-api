# books-api

Welcome to **BooksAPI**, it's a personal project I made. This project demonstrates how to create, read, update, and delete books from a database using RESTful approach. It's really simple. You also get to query books based on genre, author, publication year, etc.


## Features

- **GET Books**: Get 10 books from the database, or you could specify the number
- **GET Books by id**: Get a single book using the id of the book
- **POST Books**: Add a new book to the database, considering one doesn't already exist with the same title
- **PUT Books**: Update book info like summary, publication year, etc
- **DELETE Books by id**: Delete a book with the given id

- The get books request also has optional query parameters like getting books by genre, author, year, etc

## To Get started

Clone this repository and get inside the folder. You also need to have a virtual environment activated.

- 1. Install the required dependencies from requirements.txt
  ```bash
  pip install -r requirements.txt
  ```
- 2. Use uvicorn to start the server
  ```bash
  uvicorn app:app --reload
  ```
- 3. Open the link uvicorn gives you
  ```bash
  http://127.0.0.1:8000/docs
  ```
  You can use FastAPI's Swagger UI or whatever you like


### API Endpoints

#### Base URL: `http://127.0.0.1:8000`

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | `/books`         | Get a list of all books  |
| GET    | `/books/{id}`    | Get details of a book    |
| POST   | `/books`         | Add a new book           |
| PUT    | `/books/{id}`    | Update an existing book  |
| DELETE | `/books/{id}`    | Delete a book            |

## Project Structure

```
books-api/
├── app.py               # Application entry point
├── database.py          # database creation
├── models.py            # Data models
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

See ya nerds