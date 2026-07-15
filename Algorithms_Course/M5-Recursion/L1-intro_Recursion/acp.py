# My Countdown Timer Challenge

# Countdown using recursion
def countdown(n):
    if n == 0:          # Base case
        print("Blast Off!")
        return

    print("Countdown:", n)
    countdown(n - 1)


# Count up while recursion unwinds
def countup(n):
    if n == 0:          # Base case
        print(0)
        return

    countup(n - 1)
    print(n)


# Demonstrating recursive call stack
def show_calls(n):
    if n == 0:
        print("Reached Base Case")
        return

    print("Calling:", n)
    show_calls(n - 1)
    print("Returning:", n)


# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:     # Base case
        return 1

    return n * factorial(n - 1)


# Main Program
number = int(input("Enter a positive number: "))

print("\n--- Countdown ---")
countdown(number)

print("\n--- Count Up ---")
countup(number)

print("\n--- Recursive Call Demonstration ---")
show_calls(number)

print("\n--- Factorial ---")
print(f"{number}! =", factorial(number))