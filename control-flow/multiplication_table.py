# Multiplication Table Generator
# Uses a for loop to generate multiplication table from 1 to 10

# Get the number from user
number = int(input("Enter a number to see its multiplication table: "))

# Generate multiplication table using for loop
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")