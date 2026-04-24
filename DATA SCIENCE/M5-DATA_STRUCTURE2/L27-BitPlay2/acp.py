def reverse_bits(n):
    result = 0

    while n > 0:
        bit = n & 1          # get last bit
        result = (result << 1) | bit
        n = n >> 1          # shift right

    return result


# Input
num = int(input("Enter a number: "))

# Output
print("Reversed bits number:", reverse_bits(num))