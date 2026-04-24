def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Find all 2-digit prime numbers
print("2-digit prime numbers are:")

for number in range(10, 100):
    if is_prime(number):
        print(number, end=" ")