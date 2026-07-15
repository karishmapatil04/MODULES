# Compare Rabin-Karp and KMP Algorithms

# ---------- Rabin-Karp Algorithm ----------
def rabin_karp(text, pattern):
    d = 256
    q = 101

    n = len(text)
    m = len(pattern)
    h = 1
    p = 0
    t = 0
    positions = []

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                positions.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return positions


# ---------- KMP Algorithm ----------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    positions = []
    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            positions.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


# ---------- Main Program ----------
text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

rk_result = rabin_karp(text, pattern)
kmp_result = kmp(text, pattern)

print("\nRabin-Karp Result:")
if rk_result:
    print("Pattern found at positions:", rk_result)
else:
    print("Pattern not found.")

print("\nKMP Result:")
if kmp_result:
    print("Pattern found at positions:", kmp_result)
else:
    print("Pattern not found.")