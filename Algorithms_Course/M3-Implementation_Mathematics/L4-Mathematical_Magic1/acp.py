# Binary to Decimal Converter

binary = input("Enter a binary number: ")

decimal = 0
power = 0

# Convert binary to decimal
for digit in binary[::-1]:
    if digit == '1':
        decimal += 2 ** power
    power += 1

print("Decimal Number:", decimal)