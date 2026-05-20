from fastapi import Body, FastAPI,Query,Path
from pydantic import BaseModel,Field
from typing import Optional


app = FastAPI()

class Book:
    id: Optional[int]=None
    title: str
    author: str 
    description: str 
    rating: float 
    published_date: int
    def __init__(self, id, title, author, description, rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date=published_date

class BookRequest(BaseModel):
    id : int = Field(description="Id is not compulsory",default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3,max_length=100)
    rating: float = Field(gt=-1,lt=6)
    published_date: int

    model_config={
        "json_schema_extra":{
            "example":{
                "title":"New Book",
                "author":"Meeran",
                "description":"New Description",
                "rating":5,
                "published_date":2000
            }
        }
    }
Books = [
    Book(1, "thinking fast and slow", "idk", "It's so awesome", 4,2000),
    Book(2, "influence","idk","I haven't read it yet",4,2019),
    Book(3, "how to win friends and influence people", "cale", "It's spectaculus", 3.8,2020),
    Book(4, "Never split the difference", "idk", "It must be good", 3.9,2021),
    Book(5, "book5", "idk", "dummy", 4,2000),
    Book(6, "book5", "idk", "dummy", 4,2000)
]

@app.get("/books/")
async def all_books():
    return Books
@app.get("/books/get_book/{book_id}")
async def get_book_with_id(book_id:int = Path(gt=0)):
    for i in range(len(Books)):
        if Books[i].id == book_id:
            return Books[i]
@app.get("/books/get_multiple_books_by_id/")
async def multiple_books_by_id(book_ids: list[int] = Query(default=[])):
    return [Book for Book in Books if Book.id in book_ids]

@app.get("/books/fetch_book_by_rating")
async def fetch_book_by_rating(rating:float =Query(ge=1,le=5)):
     return [Book for Book in Books if Book.rating == rating]

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(Books)):
        if Books[i].id==book.id:
            Books[i]=Book(**book.model_dump())

@app.get("/books/by_published_date/")
async def by_published_date(published_date:int = Query(ge=1900,le=2031)):
     return [Book for Book in Books if Book.published_date == published_date]



@app.post("/books/new_books/")
async def new_books(book_request: BookRequest):
    new_book=Book(**book_request.model_dump())
    book_find_bookid(new_book)
    print(type(new_book.id))
    Books.append(new_book)
    return "You're book is added successfully"

def book_find_bookid(book: Book):
    if len(Books)>0:
        book.id=Books[-1].id+1
    else:
        book.id=1
@app.delete("/book/delete_book/{book_id}")
async def delete_book(book_id:int):
    for i in range(len(Books)):
        if Books[i].id == book_id:
            Books.pop(i)
            break