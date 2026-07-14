# ── SCORE TRACKER ─────────────────────────────────────────────────────────────
# Topics: Asymptotic Analysis | Big-O | Omega | Theta
#         Best / Worst / Average Case | O(1) O(n) O(n^2)


# ── PART 1: The leaderboard ───────────────────────────────────────────────────
# Five players and their scores. We will run three operations
# and classify each one with formal asymptotic notation.

names  = ["Aarav", "Priya", "Dev", "Meera", "Kabir"]
scores = [90,      75,      88,    62,       95]
n = len(scores)
print("=== Score Tracker (n =", n, "players) ===")
for i in range(n):
    print(i + 1, ". ", names[i], " : ", scores[i], sep="")
print()


# ── PART 2: Theta(1) — direct index access ────────────────────────────────────
# Get the score at position 0: always exactly 1 step.
# Best case = worst case = exactly 1. That is Theta(1) — a tight bound.
# The cost never changes no matter how many players there are.

steps = 1
print("Score at index 0 :", scores[0], "| steps =", steps, "| Theta(1) - tight bound")
print()


# ── PART 3: O(n) — linear search, best and worst case ────────────────────────
# Search for a name by scanning from the very start.
# Omega(1) best case  : name is at position 0, found in 1 step.
# O(n)    worst case  : name is at position n-1, found after n steps.

target = "Aarav"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Search for", target, "| steps =", steps, "| Omega(1) - best case lower bound")

target = "Kabir"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Search for", target, "| steps =", steps, "| O(n) =", n, "- worst case upper bound")
print()


# ── PART 4: O(n^2) — find all pairs with a score sum of 150 ──────────────────
# Compare every player against every other player: a loop inside a loop.
# Asymptotic analysis: actual steps = n*(n-1)/2.
# Dominant term after dropping constants -> n^2. Big-O is O(n^2).

steps = 0
target_sum = 150
print("Pairs with total score =", target_sum, ":")
for i in range(n):
    for j in range(i + 1, n):
        steps += 1
        if scores[i] + scores[j] == target_sum:
            print(" ", names[i], "+", names[j], "=", scores[i] + scores[j])
print("Total comparisons :", steps, "| O(n^2) - drop constants, keep n^2")
print()


# ── PART 5: Asymptotic Summary ────────────────────────────────────────────────
# Asymptotic analysis: only the dominant (fastest-growing) term matters.
# Example: 3n^2 + 5n + 9 -> O(n^2). Smaller terms become irrelevant at large n.

print("=== Asymptotic Summary ===")
print("Theta(1) : index access - always 1 step, tight bound")
print("Omega(1) : best case    - found in 1 step, lower bound")
print("O(n)     : worst case   - found after n =", n, "steps, upper bound")
print("O(n^2)   : pair check   - n*(n-1)/2 =", n * (n - 1) // 2, "comparisons")
print()
print("Drop constants. Keep the dominant term. That is asymptotic analysis!")
