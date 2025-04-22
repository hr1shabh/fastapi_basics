from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title' : 'title one', 'author': 'author1', 'category': 'science'},
    {'title': 'title two', 'author': 'author2', 'category': 'science'},
    {'title': 'title three', 'author': 'author3', 'category': 'history'},
    {'title': 'title four', 'author': 'author4', 'category': 'maths'},
    {'title': 'title five', 'author': 'author2', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get('/books/')
async def read_book_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/{author}/')
async def read_book_by_author_and_category(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post('/books/create')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

@app.get('/books/get_books_by_author/{author}')
async def get_books_by_author(author: str):
    return_list = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            return_list.append(book)
    return return_list

