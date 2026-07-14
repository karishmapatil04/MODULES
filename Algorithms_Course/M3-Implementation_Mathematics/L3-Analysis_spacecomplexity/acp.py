# My Train Seat Finder

# Sorted list of seat numbers
seats = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

target = int(input("Enter seat number to search: "))

# Iterative Binary Search
def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Recursive Binary Search
def recursive_binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target)
    else:
        return recursive_binary_search(arr, low, mid - 1, target)

# Iterative Search
result = iterative_binary_search(seats, target)

if result != -1:
    print("\nIterative Binary Search: Seat found at index", result)
else:
    print("\nIterative Binary Search: Seat not found.")

# Recursive Search
result = recursive_binary_search(seats, 0, len(seats) - 1, target)

if result != -1:
    print("Recursive Binary Search: Seat found at index", result)
else:
    print("Recursive Binary Search: Seat not found.")

# Complexity Comparison
print("\nComplexity Comparison")
print("Iterative Binary Search")
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")

print("\nRecursive Binary Search")
print("Time Complexity: O(log n)")
print("Space Complexity: O(log n) (Call Stack)")

print("\nComplexity Ladder:")
print("O(1) < O(log n) < O(n) < O(n²)")