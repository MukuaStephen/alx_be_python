monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are $", monthly_savings)
annual_saving = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
annual_saving = int(annual_saving)
print("Projected savings after one year, with interest, is: $", annual_saving)