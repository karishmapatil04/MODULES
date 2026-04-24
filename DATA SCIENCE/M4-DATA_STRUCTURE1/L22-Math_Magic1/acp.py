def binary_to_decimal(binary):
    decimal = 0
    power = 0

    while binary > 0:
        digit = binary % 10          # get last digit
        decimal += digit * (2 ** power)
        binary = binary // 10        # remove last digit
        power += 1

    return decimal


# Input
binary = int(input("Enter binary number: "))

# Output
print("Decimal value:", binary_to_decimal(binary))