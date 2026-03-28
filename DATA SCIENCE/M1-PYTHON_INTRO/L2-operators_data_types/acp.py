# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("\nBefore swapping:")
print("a =", a, "b =", b, "c =", c)

# Swapping logic (a → b, b → c, c → a)
temp = a
a = b
b = c
c = temp

print("\nAfter swapping:")
print("a =", a, "b =", b, "c =", c)