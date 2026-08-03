# Program to print all permutations of a given string

def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            # Swap characters
            s[l], s[i] = s[i], s[l]

            # Recur for the remaining characters
            permute(s, l + 1, r)

            # Backtrack (swap back)
            s[l], s[i] = s[i], s[l]


# Main Program
string = input("Enter a string: ")

s = list(string)
print("All permutations are:")
permute(s, 0, len(s) - 1)