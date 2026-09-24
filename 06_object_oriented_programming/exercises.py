"""OOP exercises: composition and an extensible library model."""

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title, self.author = title, author
        self.is_checked_out = False

class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add(self, book: Book) -> None:
        self.books.append(book)

    def checkout(self, title: str) -> None:
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                return
        raise ValueError("book unavailable")
