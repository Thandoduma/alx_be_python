# Robust Division Calculator
# Handles division with comprehensive error checking

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling.
    
    Args:
        numerator: The numerator (can be string or number)
        denominator: The denominator (can be string or number)
        
    Returns:
        str: Success message with result or error message
    """
    try:
        # Convert inputs to float (may raise ValueError)
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division (may raise ZeroDivisionError)
        result = num / denom
        
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."