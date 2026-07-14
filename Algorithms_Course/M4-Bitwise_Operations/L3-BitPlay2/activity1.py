# ODD HUNT
# Topics: XOR Identity | XOR Cancellation | One Odd Occurring | XOR of Two | Split by Set Bit

a, b = 7, 7

# PART 1: XOR Identity and Equality
print("=== Odd Hunt ===")
print("a ^ a =", a ^ a)
print("a ^ 0 =", a ^ 0)
print("Equal (XOR):", (a ^ b) == 0)
print()

# PART 2: XOR Cancellation
arr = [3, 5, 3, 5, 9]
result = 0
for n in arr: result ^= n
print("XOR of", arr, "=", result)
print()

# PART 3: One Odd-Occurring Number
nums = [4, 7, 4, 2, 7, 2, 9]
res = 0
for n in nums: res ^= n
print("Odd occurring:", res)
print()

# PART 4: XOR of Two Odd-Occurring Numbers
pair = [3, 9, 3, 5, 5, 7]
xab = 0
for n in pair: xab ^= n
print("XOR of two odds:", xab, "->", bin(xab))
print()

# PART 5: Split by Rightmost Set Bit
setbit = xab & -xab
x, y = 0, 0
for n in pair:
    if n & setbit: x ^= n
    else: y ^= n
print("Two odd-occurring:", x, "and", y)
