def all_substrings(s):
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(s[i:j])


# Input
string = input("Enter a string: ")

# Output
print("All substrings are:")
all_substrings(string)