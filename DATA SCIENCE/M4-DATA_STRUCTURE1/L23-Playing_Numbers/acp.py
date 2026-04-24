def find_lcm(a, b):
    # Find the greater number
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


# Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Output
print("LCM is:", find_lcm(num1, num2))