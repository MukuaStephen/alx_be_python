number = input("Enter the size of the pattern:")
number = int(number)
if number > 0:
    row = 0
    while row < number:
        for col in range(number):
            print("*", end=" ")
        print()
        row += 1
else:
    print("Invalid input. Please enter a positive integer.")