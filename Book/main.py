from fastapi import FastAPI
from book import Book, BookItem

app = FastAPI()

BOOKS = [
    Book(1, "title 1", "author 1", "description 1", 1),
    Book(2, "title 2", "author 2", "description 2", 2),
    Book(3, "title 3", "author 3", "description 3", 3),
    Book(4, "title 4", "author 4", "description 4", 4),
    Book(5, "title 5", "author 5", "description 5", 5),
]


# retrieve all books
@app.get("/books")
async def all_books():
    return BOOKS


# handel IDs of books
def handel_ids(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


# create a new book
@app.post("/create-book")
async def create_book(book_item: BookItem):
    new_book = Book(**book_item.model_dump())
    BOOKS.append(handel_ids(new_book))
    return BOOKS
