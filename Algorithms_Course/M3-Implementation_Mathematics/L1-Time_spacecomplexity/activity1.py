# ── ALGORITHM ANALYSIS — Counting Game Points ─────────────────────────────────
# Topics: Algorithm | Pseudocode | Time Complexity | Space Complexity
#         One Problem Three Solutions | Comparing Efficiency


# ── PART 1: The problem — set n = 4 rounds ───────────────────────────────────
# In a game: Round 1 = 1 point, Round 2 = 2 points, ... Round n = n points.
# We will solve "find the total" THREE ways and count the steps each one takes.

n = 4
print("=== Counting Game Points (n =", n, "rounds) ===")
print()


# ── PART 2: Formula way — always 1 step ──────────────────────────────────────
# Algorithm  : Use the shortcut formula to get the answer instantly
# Pseudocode : total = n * (n + 1) / 2
# Time cost  : 1 step — stays the same no matter how big n is
# Space cost : 1 variable (total)

total = n * (n + 1) // 2
print("Formula way : total =", total, "| steps = 1")


# ── PART 3: Loop way — n steps ────────────────────────────────────────────────
# Algorithm  : Add each round's points one by one using a loop
# Pseudocode : FOR round FROM 1 TO n: total = total + round
# Time cost  : n steps — grows with the number of rounds
# Space cost : 2 variables (total, round_num)

total = 0
steps = 0
for round_num in range(1, n + 1):
    total += round_num
    steps += 1
print("Loop way    : total =", total, "| steps =", steps)


# ── PART 4: Nested loop way — roughly n*n steps ───────────────────────────────
# Algorithm  : Add 1 at a time for every single point in every round
# Pseudocode : FOR round FROM 1 TO n: FOR point FROM 1 TO round: total += 1
# Time cost  : roughly n*n steps — explodes as n grows!
# Space cost : 3 variables (total, round_num, point)

total = 0
steps = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        total += 1
        steps += 1
print("Nested loop : total =", total, "| steps =", steps)


# ── PART 5: Try n = 10 and see what happens to the steps ─────────────────────
n = 10
nested_steps = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        nested_steps += 1

print()
print("=== Now with n =", n, "rounds ===")
print("Formula way : steps = 1        (always just 1!)")
print("Loop way    : steps =", n)
print("Nested loop : steps =", nested_steps, "(grows much faster!)")
print()
print("Same answer — but very different costs. That is time complexity!")
