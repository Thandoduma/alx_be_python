# Simple Calculator with Match Case
# Uses Match Case statements to perform arithmetic operations

# Get user input for the two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the operation from user
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")