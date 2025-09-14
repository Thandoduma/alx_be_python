# Personal Finance Calculator
# Calculates monthly savings and projects annual savings with interest

# Get user input for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
# Formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
annual_interest_rate = 0.05
annual_savings_without_interest = monthly_savings * 12
interest_earned = annual_savings_without_interest * annual_interest_rate
projected_savings = annual_savings_without_interest + interest_earned

# Display results
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")