# Remove duplicate characters from a string

string = input("Enter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result += ch

print("String after removing duplicate characters:", result)