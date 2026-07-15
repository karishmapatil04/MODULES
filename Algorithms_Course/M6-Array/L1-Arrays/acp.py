# Array Reverse

n = int(input("Enter the number of elements: "))

arr = []

print("Enter the array elements:")
for i in range(n):
    arr.append(int(input()))

# Reverse the array
arr.reverse()

print("Reversed Array:")
for i in arr:
    print(i, end=" ")