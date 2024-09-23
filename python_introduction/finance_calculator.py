income = input("Enter your monthly income:")
income = int(income)
expenses = input("Enter your total monthly expenses:")
expenses = int(expenses)
month_saving = income - expenses
print("Your monthly savings are $", month_saving)
annual_saving = month_saving * 12 + (month_saving * 12 * 0.05)
annual_saving = int(annual_saving)
print("Projected savings after one year, with interest, is: $", annual_saving)