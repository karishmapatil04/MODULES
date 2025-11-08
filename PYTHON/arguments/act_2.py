# Function to calculate factorial
def factorial(n):
    '''This function is for recursive function'''
    if n == 0 or n == 1:  # Base case: 0! and 1! are both 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Input from user
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(factorial.__doc__)
    print(f"The factorial of {num} is {factorial(num)}")