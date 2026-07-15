# LastOccurrence using Linear Search

n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the array elements: ").split()))

target = int(input("Enter the target element: "))

last_index = -1

# Linear Search
for i in range(n):
    if arr[i] == target:
        last_index = i

if last_index != -1:
    print("Last Occurrence Index =", last_index)
else:
    print("Element not found")