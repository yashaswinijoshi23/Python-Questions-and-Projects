print("Welcome to the Basic Calculator!")

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b 


def calculator():
    operation = int(input("Select operation: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division"))
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if operation >= 3:
        print("Invalid request. Please enter a valid operation between 1 and 4")
    if operation == 1:
        print(f"{a} + {b} = {add(a, b)}")
    elif operation == 2:
        print(f"{a} - {b} = {subtract(a, b)}")
    elif operation == 3:
        print(f"{a} * {b} = {multiply(a, b)}")
    elif operation ==  4:
        print(f"{a} / {b} = {divide(a, b)}")
    else:
        print("Invalid operation selected. Please try again.")

calculator()

