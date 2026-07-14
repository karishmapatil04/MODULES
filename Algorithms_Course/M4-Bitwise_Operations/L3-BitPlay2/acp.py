# Binary Clue Investigator

print("===== Binary Clue Investigator =====")

# Input numbers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# XOR of all numbers
xor_all = 0
for num in numbers:
    xor_all ^= num

print("\nXOR of all numbers:", xor_all)

# If only one number occurs odd number of times
print("\nIf there is only one odd-occurring number:")
print("Odd-occurring Number:", xor_all)

# Find two odd-occurring numbers
rightmost_set_bit = xor_all & -xor_all

group1 = 0
group2 = 0

for num in numbers:
    if num & rightmost_set_bit:
        group1 ^= num
    else:
        group2 ^= num

print("\nIf there are two odd-occurring numbers:")
print("First Odd-occurring Number :", group1)
print("Second Odd-occurring Number:", group2)

print("\n===== Investigation Complete =====")