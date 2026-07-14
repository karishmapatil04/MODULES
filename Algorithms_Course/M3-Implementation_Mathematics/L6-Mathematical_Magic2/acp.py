# Two-Digit Prime Numbers

print("Two-Digit Prime Numbers are:")

for num in range(10, 100):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")