# Array Energy Tracker using Kadane's Algorithm

# Function to find Maximum Subarray Sum
def max_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])

        if current_sum > max_sum:
            max_sum = current_sum

    print("Maximum Subarray Sum =", max_sum)


# Main Program
while True:
    print("\n===== Array Energy Tracker =====")
    print("1. Find Maximum Subarray Sum")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        arr = list(map(int, input("Enter array elements: ").split()))

        if len(arr) == 0:
            print("Array is empty.")
        else:
            max_subarray_sum(arr)

    elif choice == 2:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")