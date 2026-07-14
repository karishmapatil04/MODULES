# BIT PLAY
# Topics: Set Bits & Zeros | Count Set Bits | First Set Bit | Bit Masks | Check Nth Bit

n = 52   # binary: 110100

def bits(n): return bin(n)[2:]

# PART 1: Set Bits and Zero Bits
print("=== Bit Play ===")
print("n =", n, "->", bits(n))
print("Set bits  (1s):", bits(n).count('1'))
print("Zero bits (0s):", bits(n).count('0'))
print()

# PART 2: Counting Set Bits
count, temp = 0, n
while temp:
    if temp & 1: count += 1
    temp >>= 1
print("Set bits in", n, ":", count)
print()

# PART 3: The First Set Bit
pos, temp = 1, n
while temp:
    if temp & 1: break
    pos += 1
    temp >>= 1
print("First set bit of", n, "-> position", pos)
print()

# PART 4: Building a Bit Mask
print("Bit masks (1 << i):")
for i in range(6):
    print(f"  1 << {i} = {1 << i:2d} -> {bits(1 << i)}")
print()

# PART 5: Check if Nth Bit is Set
print("Bits of", n, "->", bits(n) + ":")
for bit in range(1, 7):
    result = "SET" if n & (1 << (bit - 1)) else "NOT SET"
    print(f"  bit {bit}:", result)
