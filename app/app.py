from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class BookCreator(BaseModel):
    title : str
    author : str
    year : int | None = None

class BookUpdate(BaseModel):
    title : str | None = None
    author : str | None = None
    year : int | None = None

class Book(BookCreator):
    id : int

books : list[Book] = []
next_id = 1

@app.get("/books")
def get_books():
    return books


@app.post("/books", status_code=201)
def create_book(data : BookCreator):
    global next_id
    book = Book(id = next_id, **data.model_dump)
    books.append(book)
    next_id += 1
    return book

@app.put("/books/{id}", response_model=Book)
def get_book():
    for book in books:
        if book.id == id : 
            return book
    raise HTTPException(status_code=404, detail="Book Not Found!")

@app.patch("/books/{id}", response_model=Book, status_code=status.HTTP_200_OK)
def update_book(id:int, update_data:BookUpdate):
    for book in books:
        if book.id == id:
            fields_to_update = update_data.model_dump(exclude_unset=True)

            for key, value in fields_to_update.items():
                setattr(book, key, value)

            return book

    raise HTTPException(status_code=404, detail="Book Doesnt Exist")


@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int):
    for index, book in enumerate(books):
        if book.id == id:
            books.pop(index)
            return "Book Deleted!"
    raise HTTPException(status_code=404, detail="Book Not Found!!")