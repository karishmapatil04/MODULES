# Remove all whitespace characters

text = input("Enter a string: ")

result = "".join(text.split())

print("String after removing all whitespace:")
print(result)