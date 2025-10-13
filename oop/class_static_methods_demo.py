# class_static_methods_demo.py
# Demonstrates the difference between class methods and static methods

class Calculator:
    """A calculator class demonstrating class methods and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not need access to class or instance data.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Has access to class attributes through cls parameter.
        
        Args:
            cls: The class itself (automatically passed)
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        # Accessing class attribute using cls
        print(f"Calculation type: {cls.calculation_type}")
        return a * b