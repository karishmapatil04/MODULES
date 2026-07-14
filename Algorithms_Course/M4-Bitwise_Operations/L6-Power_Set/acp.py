# Binary Subset Builder

print("===== Binary Subset Builder =====")

# Input list
items = input("Enter list items separated by spaces: ").split()
n = len(items)

print("\nOriginal List:", items)

# Generate Power Set using Binary Masks
print("\nPower Set:")
for mask in range(1 << n):      # 2^n subsets
    subset = []
    for i in range(n):
        if mask & (1 << i):     # Bit probe
            subset.append(items[i])
    print(subset)

# Check an individual bit
number = int(input("\nEnter a number for bit probe: "))
position = int(input("Enter bit position (0 = LSB): "))

if number & (1 << position):
    print(f"Bit at position {position} is SET (1).")
else:
    print(f"Bit at position {position} is NOT SET (0).")

# Compare bit difference between two numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

difference = a ^ b
count = bin(difference).count("1")

print("\nBit Difference (XOR):", bin(difference))
print("Number of Different Bits:", count)

print("\n===== Builder Complete =====")