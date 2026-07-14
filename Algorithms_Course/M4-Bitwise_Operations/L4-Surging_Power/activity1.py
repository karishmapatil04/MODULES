# POWER SURGE
# Topics: n&(n-1) Trick | Power of 2 | Power of 4 | Power of 8 | Binary Exponentiation

n = 12   # binary: 1100

# PART 1: The n & (n-1) Trick
print("=== Power Surge ===")
print("n       =", n, "->", bin(n))
print("n - 1   =", n - 1, "->", bin(n - 1))
print("n&(n-1) =", n & (n - 1), "->", bin(n & (n - 1)))
print()

# PART 2: Power of 2 Check
print("Power of 2 check:")
for x in [1, 4, 6, 16, 18, 64]:
    result = x > 0 and (x & (x - 1)) == 0   # True if only one bit is set
    print(" ", x, "->", bin(x), "->", result)
print()

# PART 3: Power of 4 Check
def pow4(n):
    if n <= 0 or n & (n - 1) != 0:   # must be a power of 2 first
        return False
    count = 0
    while n > 1:
        n = n >> 1   # right-shift: move one bit to the right
        count = count + 1
    return count % 2 == 0   # power of 4 means the bit is at an even position

print("Power of 4 check:")
for x in [1, 4, 8, 16, 32, 64]:
    print(" ", x, "->", pow4(x))
print()

# PART 4: Power of 8 Check
def pow8(n):
    if n <= 0 or n & (n - 1) != 0:   # must be a power of 2 first
        return False
    count = 0
    while n > 1:
        n = n >> 1   # right-shift: move one bit to the right
        count = count + 1
    return count % 3 == 0   # power of 8 means the bit position is divisible by 3

print("Power of 8 check:")
for x in [1, 8, 16, 64, 32, 512]:
    print(" ", x, "->", pow8(x))
print()

# PART 5: Binary Exponentiation
def fast_power(base, exp):
    result = 1
    while exp > 0:
        if exp & 1:              # check if exponent is odd
            result = result * base
        base = base * base       # square the base
        exp = exp >> 1           # halve the exponent
    return result

print("Binary exponentiation:")
print("  6 ^ 5  =", fast_power(6, 5))
print("  2 ^ 10 =", fast_power(2, 10))
print("  3 ^ 8  =", fast_power(3, 8))
