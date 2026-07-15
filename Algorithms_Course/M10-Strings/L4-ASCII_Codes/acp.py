# Find ASCII value of each character in a string

string = input("Enter a string: ")

print("Character\tASCII Value")
for ch in string:
    print(ch, "\t\t", ord(ch))