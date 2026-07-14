# BIT EXPLORER
# Topics: Bits & Binary | AND & OR | NOT & XOR | Shifts | Odd/Even | Count Bits

a = 10   # binary: 1010
b = 6    # binary: 0110

def bits(n, width=4):
    return format(n & ((1 << width) - 1), f'0{width}b')

# PART 1: Bits and Binary
print("=== Bit Explorer ===")
print("a =", a, "->", bits(a))
print("b =", b, "->", bits(b))
print()

# PART 2: AND and OR
print("AND  a & b =", a & b,      "->", bits(a & b))    # both 1 = 1
print("OR   a | b =", a | b,      "->", bits(a | b))    # either 1 = 1
print()

# PART 3: NOT and XOR
print("NOT  ~a    =", ~a & 0xFF,  "->", bits(~a, 8))    # flip all bits
print("XOR  a ^ b =", a ^ b,      "->", bits(a ^ b))    # different = 1
print()

# PART 4: Left Shift and Right Shift
print("LEFT  a << 1 =", a << 1, " (a x 2)")
print("RIGHT a >> 1 =", a >> 1, " (a / 2)")
print()

# PART 5: Odd or Even with XOR
print("Odd or Even:")
for n in [7, 10, 15, 4]:
    result = "Even" if n ^ 1 == n + 1 else "Odd"
    print(n, "->", result)
print()

# PART 6: Count Bits
def count_bits(n):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count

print("Bit count:")
for n in [a, b, 255]:
    print(n, "->", count_bits(n), "bits |", bits(n, count_bits(n)))
