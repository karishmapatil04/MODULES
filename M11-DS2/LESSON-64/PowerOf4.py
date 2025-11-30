def power4(number):
    if number <= 0:
        return False
    # Check if number is power of 2
    if (number & (number - 1)) != 0:
        return False
    # Check if the set bit is in the correct position for power of 4
    return (number & 0x55555555) != 0  # mask: 0101...0101 in binary

# Example usage
n = int(input("Enter a number: "))
if power4(n):
    print("\nThe number is a power of 4")
else:
    print("\nThe number is not a power of 4")
