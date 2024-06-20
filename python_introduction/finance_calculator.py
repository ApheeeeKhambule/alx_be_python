# finance_calculator.py

# Prompt the user to input their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
total_expenses = float(input("Enter your total monthly expenses: "))

# We will indirectly calculate monthly savings in the next steps without assigning directly

# Calculate the annual savings first
annual_savings = (monthly_income * 12) - (total_expenses * 12)

# Calculate the projected savings after one year with interest
annual_interest_rate = 0.05
projected_savings = annual_savings + (annual_savings * annual_interest_rate)

# Print the results
print(f"Your monthly savings are ${annual_savings / 12:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")


