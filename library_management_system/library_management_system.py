class Book:
    def __init__(self,isbn,title,author,publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author,publication_year):
        if isbn not in self.books:
            self.books[isbn] = Book(isbn, title, author, publication_year)

    def borrow_book(self, isbn):
        if isbn in self.books and self.books[isbn].available:
            self.books[isbn].available = False
        else:
            return ValueError(f"Book with ISBN {isbn} is not available or not available.")

    def return_book(self, isbn):
        if isbn in self.books and not self.books[isbn].available:
            self.books[isbn].available = True
        else:
            return ValueError(f"Book with ISBN {isbn} was not borrow or does not exist.")

    def view_available_books(self):
        return [book.title for book in self.books.values() if book.available]
