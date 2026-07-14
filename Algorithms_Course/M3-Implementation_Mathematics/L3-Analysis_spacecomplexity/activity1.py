# QUIZ SCORE FINDER
# Topics: O(log n) | Binary Search | Recursion | Recursive Time | Space | Complexity Ladder


# PART 1: Setup — 10 sorted quiz scores, target = 98, three search methods

scores = [12, 25, 33, 41, 50, 67, 72, 85, 91, 98]
n, target = len(scores), 98
print("=== Quiz Score Finder (n =", n, "scores) ===")
print("Scores:", scores, "| Target:", target)
print()


# PART 2: Linear Search — O(n)
# Scans every score from the start. Target at the end = worst case = n steps.

steps = 0
for i in range(n):
    steps += 1
    if scores[i] == target:
        print("Linear search  : index =", i, "| steps =", steps, "| O(n)")
        break
print()


# PART 3: Binary Search — O(log n)
# lo and hi mark the search window. mid is the midpoint. Each step halves the window.

lo, hi, steps = 0, n - 1, 0
while lo <= hi:
    mid = (lo + hi) // 2
    steps += 1
    if scores[mid] == target:
        print("Binary search  : index =", mid, "| steps =", steps, "| O(log n)")
        break
    elif scores[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
print()


# PART 4: Recursive Binary Search — O(log n) time, O(log n) stack space
# Same logic as PART 3. The function calls a smaller version of itself.
# Each recursive call adds one frame to the call stack.

def binary_search_rec(scores, lo, hi, target, calls=0):
    calls += 1
    if lo > hi:
        return -1, calls
    mid = (lo + hi) // 2
    if scores[mid] == target:
        return mid, calls
    elif scores[mid] < target:
        return binary_search_rec(scores, mid + 1, hi, target, calls)
    else:
        return binary_search_rec(scores, lo, mid - 1, target, calls)

result, calls = binary_search_rec(scores, 0, n - 1, target)
print("Recursive search : index =", result, "| calls =", calls, "| O(log n)")
print()


# PART 5: Space Complexity and Complexity Ladder
# Iterative: O(1) space — only lo, hi, mid. Recursive: O(log n) — one frame per call.

print("=== Space and Complexity Summary ===")
print("Iterative : O(1) space  — only lo, hi, mid")
print("Recursive : O(log n) space —", calls, "stack frames for n =", n)
print()
print("Complexity ladder (n =", n, "):")
print("O(1)     : 1 step   — constant, never grows")
print("O(log n) :", steps, "steps  — halving, grows slowly")
print("O(n)     :", n, "steps  — linear, grows with n")
print("O(n^2)   :", n * n, "steps — quadratic, grows fast!")
