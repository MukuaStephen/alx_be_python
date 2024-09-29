num1 = input("Enter the first number: ")
num1 = int(num1)
num2 = input("Enter the second number: ")
num2 = int(num2)
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        print("The result is ", num1 + num2)
    case "-":
        print("The result is ", num1 - num2)
    case "*":
        print("The result is ", num1 * num2)
    case "/":
        print("The result is ", num1 / num2)
    case _:
        print("Invalid operation")