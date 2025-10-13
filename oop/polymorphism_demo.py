# polymorphism_demo.py
# Demonstrates polymorphism and method overriding in Python

import math


class Shape:
    """Base class for all shapes. Defines the interface for area calculation."""
    
    def area(self):
        """
        Calculate the area of the shape.
        This method must be overridden by derived classes.
        
        Raises:
            NotImplementedError: If not overridden in derived class
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Rectangle shape that inherits from Shape."""
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Circle shape that inherits from Shape."""
    
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area (π × radius²)
        """
        return math.pi * (self.radius ** 2)