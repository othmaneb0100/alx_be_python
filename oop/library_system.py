# library_system.py

class Book:
    """A class representing a book."""

    def __init__(self, title, author):
        """Initialize the Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the Book instance."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """A class representing an eBook, inheriting from Book."""

    def __init__(self, title, author, file_size):
        """Initialize the EBook instance with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook instance."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """A class representing a print book, inheriting from Book."""

    def __init__(self, title, author, page_count):
        """Initialize the PrintBook instance with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook instance."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize the Library instance with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
