# Least Common Multiple (LCM)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

greater = max(num1, num2)

while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1

print("LCM of", num1, "and", num2, "is", lcm)