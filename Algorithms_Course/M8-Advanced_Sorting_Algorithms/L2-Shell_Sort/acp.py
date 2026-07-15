# SortWithShell

n = int(input("Enter the number of elements: "))

print("Enter the array elements:")
arr = list(map(int, input().split()))

# Shell Sort
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        temp = arr[i]
        j = i

        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j -= gap

        arr[j] = temp

    gap //= 2

print("Sorted Array:")
for i in arr:
    print(i, end=" ")