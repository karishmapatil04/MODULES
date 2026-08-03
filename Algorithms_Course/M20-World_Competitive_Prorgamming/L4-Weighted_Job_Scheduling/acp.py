# Average of a Stream of Numbers

n = int(input("Enter the number of elements in the stream: "))

total = 0

print("Enter the numbers:")

for i in range(1, n + 1):
    num = float(input())
    total += num
    average = total / i
    print(f"Average after {i} numbers = {average:.2f}")