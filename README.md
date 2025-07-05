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

You need to have Docker installed.
Once insatalled, go to the project directory and create a docker image like so:
```bash
docker build -t books-api .
```
And then, run this image:

```bash
docker run -p 8000:8000 books-api
```

Then open the link http://127.0.0.1:8000/docs in your browser

### API Endpoints

#### Base URL: `http://127.0.0.1:8000`

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | `/books`         | Get a list of all books  |
| GET    | `/books/{id}`    | Get details of a book    |
| POST   | `/books`         | Add a new book           |
| PUT    | `/books/{id}`    | Update an existing book  |
| DELETE | `/books/{id}`    | Delete a book            |

### Project Structure

```
books-api/
├── app.py               # Application entry point
├── database.py          # database creation
├── models.py            # Data models
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

See ya nerds