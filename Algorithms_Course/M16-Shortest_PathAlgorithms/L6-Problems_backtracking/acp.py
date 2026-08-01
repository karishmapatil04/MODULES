from collections import deque

def stepping_numbers(n, m):
    result = []

    # 0 is a stepping number
    if n == 0:
        result.append(0)

    # Start BFS from digits 1 to 9
    for i in range(1, 10):
        queue = deque([i])

        while queue:
            num = queue.popleft()

            if num > m:
                continue

            if n <= num <= m:
                result.append(num)

            last_digit = num % 10

            # Generate next stepping numbers
            if last_digit > 0:
                queue.append(num * 10 + (last_digit - 1))

            if last_digit < 9:
                queue.append(num * 10 + (last_digit + 1))

    return sorted(result)


# Input
n = int(input("Enter n: "))
m = int(input("Enter m: "))

# Output
print("Stepping Numbers:", stepping_numbers(n, m))