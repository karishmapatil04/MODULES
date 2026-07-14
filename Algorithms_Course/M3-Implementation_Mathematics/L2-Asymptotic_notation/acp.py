# My Quiz Result Searcher

# Quiz scores
scores = [85, 90, 75, 60, 95]

# -------------------------
# Method 1: Direct Access
# -------------------------
print("Method 1: Direct Access")
print("Score at index 2:", scores[2])

# -------------------------
# Method 2: Linear Search
# -------------------------
target = int(input("\nEnter score to search: "))
found = False

for i in range(len(scores)):
    if scores[i] == target:
        print("Score found at index", i)
        found = True
        break

if not found:
    print("Score not found.")

# -------------------------
# Method 3: Pair Comparison
# -------------------------
print("\nMethod 3: Pair Comparison")

for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[i] > scores[j]:
            print(scores[i], "is greater than", scores[j])

# -------------------------
# Complexity
# -------------------------
print("\nTime Complexity")
print("Direct Access : O(1)")
print("Linear Search : O(n)")
print("Pair Comparison : O(n^2)")

print("\nBest Case:")
print("Direct Access : O(1)")
print("Linear Search : O(1) (element found first)")
print("Pair Comparison : O(n^2)")

print("\nAverage Case:")
print("Linear Search : O(n)")
print("Pair Comparison : O(n^2)")

print("\nWorst Case:")
print("Linear Search : O(n)")
print("Pair Comparison : O(n^2)")

print("\nSpace Complexity: O(1)")