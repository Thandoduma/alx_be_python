# book_class.py
# Demonstrates Python magic methods (dunder methods)

class Book:
    """A class representing a book with magic methods."""
    
    def __init__(self, title, author, year):
        """
        Constructor: Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed.
        Prints a deletion message.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation for end users.
        Called by print() and str().
        
        Returns:
            str: Human-readable representation of the book
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official string representation for developers.
        Should return a string that could recreate the object.
        Called by repr() and in the interactive interpreter.
        
        Returns:
            str: String that can recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"