number = input("Enter a number to see its mutiplication table: ")
X = int(number)
for Y in range(1, 11):
    Z = X * Y
    print(f"{X} * {Y} = {Z}")