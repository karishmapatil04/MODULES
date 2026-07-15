# Find the first non-repeating character

string = input("Enter a string: ")

for ch in string:
    if string.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found.")