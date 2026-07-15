# SortWithSelection

n = int(input("Enter the number of elements: "))

print("Enter the array elements:")
arr = list(map(int, input().split()))

# Selection Sort
for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the minimum element with the current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array:")
for i in arr:
    print(i, end=" ")