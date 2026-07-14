# Power of Two Scanner

print("===== Power of Two Scanner =====")

# Input number
n = int(input("Enter a positive integer: "))

print("\nBinary Representation:", bin(n))

# Remove the rightmost set bit
if n > 0:
    removed = n & (n - 1)
    print("After Removing Rightmost Set Bit:", bin(removed))
else:
    print("Rightmost set bit removal is not applicable.")

# Check if power of 2
if n > 0 and (n & (n - 1)) == 0:
    print("\nThe number is a Power of 2.")
else:
    print("\nThe number is NOT a Power of 2.")

# Check if power of 4
if n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0:
    print("The number is a Power of 4.")
else:
    print("The number is NOT a Power of 4.")

# Check if power of 8
if n > 0 and (n & (n - 1)) == 0 and (n - 1) % 7 == 0:
    print("The number is a Power of 8.")
else:
    print("The number is NOT a Power of 8.")

# Binary Exponentiation Function
def binary_power(base, exponent):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result

# Input for binary exponentiation
base = int(input("\nEnter the base: "))
exponent = int(input("Enter the exponent: "))

print(f"{base}^{exponent} =", binary_power(base, exponent))

print("\n===== Scan Complete =====")