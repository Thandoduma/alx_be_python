# library_system.py
# Demonstrates inheritance and composition in Python OOP

class Book:
    """Base class representing a generic book."""
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        # Call parent class constructor
        super().__init__(title, author)
        # Initialize EBook-specific attribute
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book."""
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        # Call parent class constructor
        super().__init__(title, author)
        # Initialize PrintBook-specific attribute
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition by managing a collection of books."""
    
    def __init__(self):
        """Initialize a Library with an empty collection of books."""
        self.books = []  # Composition: Library HAS-A collection of books
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
    
    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)