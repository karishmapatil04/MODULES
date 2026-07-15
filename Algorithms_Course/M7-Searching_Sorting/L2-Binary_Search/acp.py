# FindMyElement using Binary Search

n = int(input("Enter the number of elements: "))

print("Enter the sorted array elements:")
arr = list(map(int, input().split()))

target = int(input("Enter the target element: "))

low = 0
high = n - 1
index = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        index = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if index != -1:
    print("Element found at index =", index)
else:
    print("Element not found")