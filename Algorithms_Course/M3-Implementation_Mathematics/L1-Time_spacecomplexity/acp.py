# My Running Lap Tracker

n = int(input("Enter the number of laps: "))

# -------------------------------
# Method 1: Formula
# -------------------------------
formula_total = n * (n + 1) // 2
print("\nMethod 1 (Formula)")
print("Total Points:", formula_total)

# -------------------------------
# Method 2: Single Loop
# -------------------------------
loop_total = 0
steps = 0

for i in range(1, n + 1):
    loop_total += i
    steps += 1

print("\nMethod 2 (Single Loop)")
print("Total Points:", loop_total)
print("Steps:", steps)

# -------------------------------
# Method 3: Nested Loop
# -------------------------------
nested_total = 0
steps = 0

for i in range(1, n + 1):
    for j in range(i):
        nested_total += 1
        steps += 1

print("\nMethod 3 (Nested Loop)")
print("Total Points:", nested_total)
print("Steps:", steps)

# -------------------------------
# Complexity Comparison
# -------------------------------
print("\nTime Complexity:")
print("Formula      : O(1)")
print("Single Loop  : O(n)")
print("Nested Loop  : O(n²)")

print("\nSpace Complexity:")
print("All Methods  : O(1)")

print("\nMost Efficient Algorithm: Formula Method (O(1))")