# Subset Sum Problem using Backtracking

def subsetSum(arr, n, target, index, currentSum, subset):
    # If target sum is found
    if currentSum == target:
        print("Subset found:", subset)
        return

    # Stop if all elements are considered or sum exceeds target
    if index == n or currentSum > target:
        return

    # Include current element
    subset.append(arr[index])
    subsetSum(arr, n, target, index + 1,
              currentSum + arr[index], subset)

    # Exclude current element (Backtrack)
    subset.pop()
    subsetSum(arr, n, target, index + 1,
              currentSum, subset)


# Main Program
n = int(input("Enter number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter target sum: "))

print("Subsets with sum", target, "are:")
subsetSum(arr, n, target, 0, 0, [])