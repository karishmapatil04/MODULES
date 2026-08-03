# Nuts & Bolts Problem using Quick Sort

def partition(arr, low, high, pivot):
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def matchPairs(nuts, bolts, low, high):
    if low < high:
        # Partition nuts using last bolt as pivot
        pivot = partition(nuts, low, high, bolts[high])

        # Partition bolts using matched nut as pivot
        partition(bolts, low, high, nuts[pivot])

        # Recur for left and right subarrays
        matchPairs(nuts, bolts, low, pivot - 1)
        matchPairs(nuts, bolts, pivot + 1, high)


# Main Program
n = int(input("Enter number of nuts and bolts: "))

print("Enter nuts:")
nuts = input().split()

print("Enter bolts:")
bolts = input().split()

matchPairs(nuts, bolts, 0, n - 1)

print("\nMatched Nuts and Bolts:")
for i in range(n):
    print(f"{nuts[i]} - {bolts[i]}")