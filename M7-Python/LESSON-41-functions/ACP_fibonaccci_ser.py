def fibonacci(n):
    first = 0
    second = 1

    for i in range(n):
        print(first, end=" ")
        next = first + second
        first = second
        second = next


# taking input from user
n = int(input("Enter number of terms: "))

print("Fibonacci Series:")
fibonacci(n)