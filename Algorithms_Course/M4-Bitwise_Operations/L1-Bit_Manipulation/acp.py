# My Secret Code Bit Scanner

# Input
secret_code = int(input("Enter the Secret Code (integer): "))
access_key = int(input("Enter the Access Key (integer): "))

print("\n===== My Secret Code Bit Scanner =====")

# Display binary values
print("Secret Code (Binary):", bin(secret_code))
print("Access Key  (Binary):", bin(access_key))

# 1. Compare bits using AND
matching_bits = secret_code & access_key
print("\n1. Matching Bits (AND):", bin(matching_bits))

# 2. Combine bits using OR
combined_bits = secret_code | access_key
print("2. Combined Bits (OR):", bin(combined_bits))

# 3. Find different bits using XOR
different_bits = secret_code ^ access_key
print("3. Different Bits (XOR):", bin(different_bits))

# 4. Flip bits of the secret code
flipped_bits = ~secret_code
print("4. Flipped Secret Code:", bin(flipped_bits))

# 5. Shift bits
left_shift = secret_code << 1
right_shift = secret_code >> 1
print("5. Left Shift by 1 :", bin(left_shift))
print("   Right Shift by 1:", bin(right_shift))

# 6. Count number of 1s in the secret code
bit_count = bin(secret_code).count("1")
print("6. Number of 1 Bits:", bit_count)

print("\n===== Scan Complete =====")