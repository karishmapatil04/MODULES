# Target Tracker Lab

# 1. Find Total Sum of Array
def total_sum(arr):
    print("Total Sum =", sum(arr))


# 2. Find Equilibrium Index
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total -= arr[i]

        if left_sum == total:
            print("Equilibrium Index =", i)
            return

        left_sum += arr[i]

    print("No Equilibrium Index Found")


# 3. Find Target Sum using Sliding Window
def target_sum(arr, target):
    start = 0
    current_sum = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == target:
            print("Target Sum Found from index", start, "to", end)
            return

    print("Target Sum Not Found")


# Main Program
while True:
    print("\n===== Target Tracker Lab =====")
    print("1. Find Total Sum")
    print("2. Find Equilibrium Index")
    print("3. Find Target Sum")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        arr = list(map(int, input("Enter array elements: ").split()))
        total_sum(arr)

    elif choice == 2:
        arr = list(map(int, input("Enter array elements: ").split()))
        equilibrium_index(arr)

    elif choice == 3:
        arr = list(map(int, input("Enter array elements: ").split()))
        target = int(input("Enter target sum: "))
        target_sum(arr, target)

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")