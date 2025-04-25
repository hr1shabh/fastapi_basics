from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    publish_date: int

    def __init__(self, id, title, author, description, rating, publish_date):
        self.id = id
        self.title = title
        self.rating = rating
        self.description = description
        self.author = author
        self.publish_date = publish_date

class Book_Request(BaseModel):
    id: Optional[int] = Field(description="Id is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    publish_date: int = Field(gt=1900, lt=2025)

BOOKS = [
    Book(1, '1984', 'Orwell', 'Great Book', 5, 1950),
    Book(2, 'Man search for meaning', 'Victor Frankl', 'Awesome Book', 5, 1970),
    Book(3, 'Atomic Habits', 'James Clear', 'Nice', 4, 2010)
]

@app.get('/books', status_code=status.HTTP_200_OK)
async def read_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_book_by_rating(rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def get_book_by_publish_date(publish_date: int = Query(lt=2025, gt=1900)):
    books_to_return = []
    for book in BOOKS:
        if book.publish_date == publish_date:
            books_to_return.append(book)
    return books_to_return

@app.post('/create-book', status_code=status.HTTP_201_CREATED)
async def create_book(book_request: Book_Request):
    new_book = Book(**book_request.dict())
    BOOKS.append(add_id(new_book))

@app.put('/books/update_book', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: Book_Request):
    book_change = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_change = True
            break
    if not book_change:
        raise HTTPException(status_code=404, detail='Item not found')

@app.delete('/books/delete_book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_change = False
    for i in range(len(BOOKS)):
        print(BOOKS[i].id)
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_change = True
            break

    if not book_change:
        raise HTTPException(status_code=404, detail='Item not found')

def add_id(book: Book):
    if len(BOOKS) == 0:
        book.id = 1
    else:
        book.id = BOOKS[-1].id + 1
    return book