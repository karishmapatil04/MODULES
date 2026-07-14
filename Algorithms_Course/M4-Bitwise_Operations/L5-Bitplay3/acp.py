# Bitwise Swap Challenge

print("===== Bitwise Swap Challenge =====")

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore Swap:")
print("a =", a)
print("b =", b)

# XOR Swap (without third variable)
a = a ^ b
b = a ^ b
a = a ^ b

print("\nAfter XOR Swap:")
print("a =", a)
print("b =", b)

# Double a number using left shift
num = int(input("\nEnter a number to double: "))
print("Double of", num, "is", num << 1)

# Detect if two numbers have different signs
x = int(input("\nEnter first number for sign check: "))
y = int(input("Enter second number for sign check: "))

if (x ^ y) < 0:
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")

# Divide without using /
dividend = int(input("\nEnter dividend: "))
divisor = int(input("Enter divisor: "))

if divisor == 0:
    print("Division by zero is not allowed.")
else:
    quotient = 0
    negative = (dividend < 0) ^ (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if negative:
        quotient = -quotient

    print("Quotient =", quotient)
    print("Remainder =", dividend)

print("\n===== Challenge Complete =====")