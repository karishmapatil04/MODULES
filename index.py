"""def add(a, b):
    return a + b  
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (1, 2, 3, 4): ")

    if operation == '1':
        result = add(num1, num2)
        print(f"The result of addition is: {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"The result of subtraction is: {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"The result of multiplication is: {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"The result of division is: {result}")
    else:
        print("Invalid operation selected.")


except ValueError: 
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")"""


import random

print(random.randint(5, 10))
print(random.random())