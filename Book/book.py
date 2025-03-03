from pydantic import BaseModel, Field
from typing import Optional


class BookItem(BaseModel):
    id: Optional[int] = Field(description="ID is not required", default=None)
    title: str = Field(min_length=5)
    author: str = Field(min_length=5)
    description: str = Field(default=None)
    rating: int = Field(gt=0, lt=6)


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
