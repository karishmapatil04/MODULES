# ASCII Value Checker

ch = input("Enter a character: ")

if len(ch) == 1:
    print("ASCII value of", ch, "is", ord(ch))
else:
    print("Please enter only one character.")