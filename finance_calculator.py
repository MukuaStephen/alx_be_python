income=input("Enter your monthly income:")
income=int(income)
expenses=input("Enter your total monthly expenses:")
expenses=int(expenses)
savings=income-expenses
print(" Your monthly savings are $", savings)
Projected_Savings = savings * 12 + (savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $", Projected_Savings)