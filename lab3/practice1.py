from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Mock database of books
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

# Pydantic model
class Book(BaseModel):
    title: str
    author: str
    year: int

# GET endpoint
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}