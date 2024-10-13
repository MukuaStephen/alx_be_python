class Book:
    """A base class to represent a book."""
    
    def __init__(self, title: str, author: str):
        """Initialize a Book instance."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the Book instance."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """A class to represent an eBook, inheriting from Book."""
    
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an EBook instance."""
        super().__init__(title, author)  # Call the constructor of the base class
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook instance."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """A class to represent a printed book, inheriting from Book."""
    
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a PrintBook instance."""
        super().__init__(title, author)  # Call the constructor of the base class
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook instance."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A class to represent a library that holds books."""
    
    def __init__(self):
        """Initialize a Library instance with an empty book collection."""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)


