# SortWithBubble

n = int(input("Enter the number of elements: "))

print("Enter the array elements:")
arr = list(map(int, input().split()))

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:")
for i in arr:
    print(i, end=" ")