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


@app.put("/books/{id}")
def update_books(id: int, book: BookUpdate):
  with Session(db) as session:
    statement = select(Book).where(Book.id == id)
    bookExists = session.exec(statement).one_or_none()

  if not bookExists:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

  if book.title: bookExists.title = book.title
  if book.author: bookExists.author = book.author
  if book.pages: bookExists.pages = book.pages

  session.add(bookExists)
  session.commit()
  session.refresh(bookExists)
  return bookExists







def addBooks():
    with Session(db) as session:
        b1 = Book(title="To Kill a Mockingbird", author="Harper Lee", pages=281,
                  summary="A novel about racial injustice in the Deep South.", 
                  publication_year=1960, genre="Fiction", language="English", is_available=True)
        b2 = Book(title="1984", author="George Orwell", pages=328,
                  summary="A dystopian novel about totalitarianism and surveillance.", 
                  publication_year=1949, genre="Dystopian", language="English", is_available=True)
        b3 = Book(title="Pride and Prejudice", author="Jane Austen", pages=279,
                  summary="A romantic novel exploring manners and marriage in 19th-century England.", 
                  publication_year=1813, genre="Romance", language="English", is_available=True)
        b4 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", pages=180,
                  summary="A story of wealth, love, and the American dream in the Jazz Age.", 
                  publication_year=1925, genre="Fiction", language="English", is_available=True)
        b5 = Book(title="Moby Dick", author="Herman Melville", pages=635,
                  summary="A whaling voyage turns into an obsession with a white whale.", 
                  publication_year=1851, genre="Adventure", language="English", is_available=False)
        b6 = Book(title="War and Peace", author="Leo Tolstoy", pages=1225,
                  summary="A sweeping narrative of Russia during the Napoleonic era.", 
                  publication_year=1869, genre="Historical Fiction", language="English", is_available=True)
        b7 = Book(title="The Catcher in the Rye", author="J.D. Salinger", pages=277,
                  summary="A young man's journey through New York City, exploring adolescence.", 
                  publication_year=1951, genre="Fiction", language="English", is_available=False)
        b8 = Book(title="Jane Eyre", author="Charlotte Brontë", pages=500,
                  summary="An orphaned girl's journey through love, morality, and independence.", 
                  publication_year=1847, genre="Romance", language="English", is_available=True)
        b9 = Book(title="The Hobbit", author="J.R.R. Tolkien", pages=310,
                  summary="A hobbit's unexpected adventure to reclaim a treasure from a dragon.", 
                  publication_year=1937, genre="Fantasy", language="English", is_available=True)
        b10 = Book(title="Fahrenheit 451", author="Ray Bradbury", pages=256,
                   summary="A dystopian world where books are outlawed and burned.", 
                   publication_year=1953, genre="Dystopian", language="English", is_available=True)
        
        b11 = Book(title="Crime and Punishment", author="Fyodor Dostoevsky", pages=671,
                   summary="A psychological drama about guilt, punishment, and redemption.",
                   publication_year=1866, genre="Psychological Fiction", language="English", is_available=True)
        b12 = Book(title="Wuthering Heights", author="Emily Brontë", pages=416,
                   summary="A passionate and tragic love story set on the Yorkshire moors.",
                   publication_year=1847, genre="Romance", language="English", is_available=True)
        b13 = Book(title="Animal Farm", author="George Orwell", pages=112,
                   summary="An allegory about the rise of totalitarianism and the Russian Revolution.",
                   publication_year=1945, genre="Satire", language="English", is_available=True)
        b14 = Book(title="The Odyssey", author="Homer", pages=541,
                   summary="An epic journey of Odysseus as he strives to return home after the Trojan War.",
                   publication_year=-800, genre="Epic Poetry", language="Greek", is_available=True)
        b15 = Book(title="Brave New World", author="Aldous Huxley", pages=311,
                   summary="A dystopian future where people are genetically engineered for their roles.",
                   publication_year=1932, genre="Science Fiction", language="English", is_available=True)
        b16 = Book(title="Les Misérables", author="Victor Hugo", pages=1488,
                   summary="The story of love, justice, and redemption set in post-revolutionary France.",
                   publication_year=1862, genre="Historical Fiction", language="French", is_available=True)
        b17 = Book(title="The Lord of the Rings", author="J.R.R. Tolkien", pages=1178,
                   summary="A young hobbit must destroy a powerful ring to prevent the end of the world.",
                   publication_year=1954, genre="Fantasy", language="English", is_available=True)
        b18 = Book(title="The Adventures of Sherlock Holmes", author="Arthur Conan Doyle", pages=307,
                   summary="A collection of stories featuring the famous detective Sherlock Holmes.",
                   publication_year=1892, genre="Mystery", language="English", is_available=True)
        b19 = Book(title="The Count of Monte Cristo", author="Alexandre Dumas", pages=1276,
                   summary="A tale of betrayal, revenge, and redemption set in 19th-century France.",
                   publication_year=1844, genre="Adventure", language="French", is_available=True)
        b20 = Book(title="Dracula", author="Bram Stoker", pages=418,
                   summary="A gothic horror novel about the infamous vampire Count Dracula.",
                   publication_year=1897, genre="Horror", language="English", is_available=True)
        
        b21 = Book(title="The Alchemist", author="Paulo Coelho", pages=208,
                   summary="A shepherd boy's journey in search of a hidden treasure.", 
                   publication_year=1988, genre="Fiction", language="Portuguese", is_available=True)
        b22 = Book(title="The Picture of Dorian Gray", author="Oscar Wilde", pages=254,
                   summary="A man stays youthful while his portrait ages, reflecting his moral decay.",
                   publication_year=1890, genre="Philosophical Fiction", language="English", is_available=True)
        b23 = Book(title="Slaughterhouse-Five", author="Kurt Vonnegut", pages=275,
                   summary="A soldier experiences time travel and recounts his experiences in World War II.",
                   publication_year=1969, genre="Science Fiction", language="English", is_available=True)
        b24 = Book(title="Anna Karenina", author="Leo Tolstoy", pages=864,
                   summary="A tragic story of love and infidelity in 19th-century Russian society.",
                   publication_year=1878, genre="Realist Fiction", language="Russian", is_available=True)
        b25 = Book(title="Frankenstein", author="Mary Shelley", pages=280,
                   summary="A scientist creates a living creature, with disastrous consequences.",
                   publication_year=1818, genre="Gothic Fiction", language="English", is_available=True)
        b26 = Book(title="The Grapes of Wrath", author="John Steinbeck", pages=464,
                   summary="A family of sharecroppers struggles to survive during the Great Depression.",
                   publication_year=1939, genre="Fiction", language="English", is_available=True)
        b27 = Book(title="One Hundred Years of Solitude", author="Gabriel García Márquez", pages=417,
                   summary="A family’s magical realism-filled story spans seven generations.",
                   publication_year=1967, genre="Magical Realism", language="Spanish", is_available=True)
        b28 = Book(title="Great Expectations", author="Charles Dickens", pages=505,
                   summary="A young orphan’s coming-of-age story in Victorian England.",
                   publication_year=1860, genre="Fiction", language="English", is_available=True)
        b29 = Book(title="Lolita", author="Vladimir Nabokov", pages=336,
                   summary="A man becomes obsessed with a young girl and the consequences of his actions.",
                   publication_year=1955, genre="Fiction", language="English", is_available=True)
        b30 = Book(title="A Tale of Two Cities", author="Charles Dickens", pages=448,
                   summary="The story of the French Revolution, highlighting sacrifice and heroism.",
                   publication_year=1859, genre="Historical Fiction", language="English", is_available=True)
        
        b31 = Book(title="The Shining", author="Stephen King", pages=659,
                   summary="A man slowly loses his mind as he watches over a haunted hotel.",
                   publication_year=1977, genre="Horror", language="English", is_available=True)
        b32 = Book(title="Of Mice and Men", author="John Steinbeck", pages=103,
                   summary="Two migrant workers in the Great Depression struggle to make a life for themselves.",
                   publication_year=1937, genre="Fiction", language="English", is_available=True)
        b33 = Book(title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", pages=193,
                   summary="A comedic space adventure about the end of the world and beyond.",
                   publication_year=1979, genre="Science Fiction", language="English", is_available=True)
        b34 = Book(title="Don Quixote", author="Miguel de Cervantes", pages=992,
                   summary="A man becomes a knight in his quest to revive chivalric virtues.",
                   publication_year=1605, genre="Novel", language="Spanish", is_available=True)
        b35 = Book(title="Rebecca", author="Daphne du Maurier", pages=428,
                   summary="A woman becomes obsessed with her husband’s first wife after their marriage.",
                   publication_year=1938, genre="Gothic Fiction", language="English", is_available=True)
        b36 = Book(title="The Brothers Karamazov", author="Fyodor Dostoevsky", pages=796,
                   summary="A philosophical exploration of faith, doubt, and family in 19th-century Russia.",
                   publication_year=1880, genre="Philosophical Fiction", language="Russian", is_available=True)
        b37 = Book(title="Dune", author="Frank Herbert", pages=688,
                   summary="A young nobleman’s journey to become the ruler of a desert planet.",
                   publication_year=1965, genre="Science Fiction", language="English", is_available=True)
        b38 = Book(title="The Road", author="Cormac McCarthy", pages=287,
                   summary="A father and son survive in a post-apocalyptic world, struggling with survival.",
                   publication_year=2006, genre="Post-apocalyptic", language="English", is_available=True)
        b39 = Book(title="Beloved", author="Toni Morrison", pages=321,
                   summary="A woman’s past haunts her as she tries to create a new life with her family.",
                   publication_year=1987, genre="Historical Fiction", language="English", is_available=True)
        b40 = Book(title="The Handmaid's Tale", author="Margaret Atwood", pages=311,
                   summary="In a dystopian future, a woman is forced into servitude in a totalitarian society.",
                   publication_year=1985, genre="Dystopian", language="English", is_available=True)
        
        b41 = Book(title="Catch-22", author="Joseph Heller", pages=453,
                   summary="A World War II bomber pilot fights to maintain his sanity in a nonsensical world.",
                   publication_year=1961, genre="Satire", language="English", is_available=True)
        b42 = Book(title="The Old Man and the Sea", author="Ernest Hemingway", pages=127,
                   summary="An old fisherman battles a giant marlin in the Gulf Stream.",
                   publication_year=1952, genre="Fiction", language="English", is_available=True)
        b43 = Book(title="Gulliver's Travels", author="Jonathan Swift", pages=352,
                   summary="A satirical adventure that critiques politics and human nature.",
                   publication_year=1726, genre="Satire", language="English", is_available=True)
        b44 = Book(title="The Secret Garden", author="Frances Hodgson Burnett", pages=279,
                   summary="A young girl finds a hidden garden and discovers its healing power.",
                   publication_year=1911, genre="Children's Fiction", language="English", is_available=True)
        b45 = Book(title="The Metamorphosis", author="Franz Kafka", pages=201,
                   summary="A man transforms into a giant insect and faces alienation and rejection.",
                   publication_year=1915, genre="Existential Fiction", language="German", is_available=True)
        b46 = Book(title="A Clockwork Orange", author="Anthony Burgess", pages=192,
                   summary="A young delinquent’s journey of violence, redemption, and free will.",
                   publication_year=1962, genre="Dystopian", language="English", is_available=True)
        b47 = Book(title="Ulysses", author="James Joyce", pages=730,
                   summary="A day in the life of three people in Dublin, exploring themes of identity.",
                   publication_year=1922, genre="Modernist Fiction", language="English", is_available=True)
        b48 = Book(title="The Bell Jar", author="Sylvia Plath", pages=244,
                   summary="A young woman struggles with mental illness and societal expectations.",
                   publication_year=1963, genre="Fiction", language="English", is_available=True)
        b49 = Book(title="Gone with the Wind", author="Margaret Mitchell", pages=1037,
                   summary="A Southern woman’s struggle to survive the American Civil War and its aftermath.",
                   publication_year=1936, genre="Historical Fiction", language="English", is_available=True)
        b50 = Book(title="The Little Prince", author="Antoine de Saint-Exupéry", pages=96,
                   summary="A young prince travels across planets, meeting various characters along the way.",
                   publication_year=1943, genre="Children's Fiction", language="French", is_available=True)

        session.add_all([b1, b2, b3, b4, b5, b6, b7, b8, b9, b10,
                         b11, b12, b13, b14, b15, b16, b17, b18, b19, b20,
                         b21, b22, b23, b24, b25, b26, b27, b28, b29, b30,
                         b31, b32, b33, b34, b35, b36, b37, b38, b39, b40,
                         b41, b42, b43, b44, b45, b46, b47, b48, b49, b50])
        session.commit()
        print("50 books added to the database!")

# addBooks()