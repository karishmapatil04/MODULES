def sum_n(n):
    return n * (n + 1) // 2  # integer result

def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total

def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)

# Examples
a = [12, 3, 4, 15]

print("Sum of first n numbers (n=5):", sum_n(5))
print("Array sum:", array_sum(a))
print("Recursive sum (n=5):", summ(5))