# Binary Streak Tracker

# 1. Count Maximum Consecutive 1s
def max_consecutive_ones(arr):
    count = 0
    maximum = 0

    for num in arr:
        if num == 1:
            count += 1
            if count > maximum:
                maximum = count
        else:
            count = 0

    print("Maximum Consecutive 1s =", maximum)


# 2. Move Zeros to the End
def move_zeros(arr):
    write = 0

    # Move all non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write] = arr[i]
            write += 1

    # Fill remaining positions with zeros
    while write < len(arr):
        arr[write] = 0
        write += 1

    print("Array after moving zeros:", arr)


# Main Program
while True:
    print("\n===== Binary Streak Tracker =====")
    print("1. Count Maximum Consecutive 1s")
    print("2. Move Zeros to the End")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        arr = list(map(int, input("Enter binary array (0s and 1s): ").split()))
        max_consecutive_ones(arr)

    elif choice == 2:
        arr = list(map(int, input("Enter array: ").split()))
        move_zeros(arr)

    elif choice == 3:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")