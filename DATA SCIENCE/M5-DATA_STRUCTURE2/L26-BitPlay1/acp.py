def rightmost_set_bit(n):
    if n == 0:
        return 0
    return n & -n


# Input
num = int(input("Enter a number: "))

# Output
result = rightmost_set_bit(num)

print("Rightmost set bit value:", result)