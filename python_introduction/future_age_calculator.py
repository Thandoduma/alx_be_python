# Future Age Calculator
# Calculates how old the user will be in 2050
# Assumes current year is 2023, so we add 27 years (2050 - 2023 = 27)

# Prompt the user for their current age
current_age = int(input("How old are you? "))

# Calculate age in 2050
# Since we assume current year is 2023, we add 27 years (2050 - 2023 = 27)
years_to_add = 27
future_age = current_age + years_to_add

# Print the result in the required format
print(f"In 2050, you will be {future_age} years old.")