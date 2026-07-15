# Score List Explorer using Recursion

# Recursive Sum
def recursive_sum(scores):
    if len(scores) == 0:
        return 0
    return scores[0] + recursive_sum(scores[1:])


# Find Largest Score
def find_largest(scores):
    if len(scores) == 1:
        return scores[0]

    largest = find_largest(scores[1:])

    if scores[0] > largest:
        return scores[0]
    else:
        return largest


# Check if List is Sorted
def is_sorted(scores):
    if len(scores) <= 1:
        return True

    if scores[0] > scores[1]:
        return False

    return is_sorted(scores[1:])


# Display Head and Tail
def head_tail(scores):
    if len(scores) == 0:
        print("The list is empty.")
    else:
        print("Head (First Score):", scores[0])
        print("Tail (Remaining Scores):", scores[1:])


# Main Program
scores = list(map(int, input("Enter scores separated by spaces: ").split()))

while True:
    print("\n===== Score List Explorer =====")
    print("1. Display Head and Tail")
    print("2. Calculate Recursive Sum")
    print("3. Find Largest Score")
    print("4. Check if Scores are Sorted")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        head_tail(scores)

    elif choice == 2:
        print("Total Sum =", recursive_sum(scores))

    elif choice == 3:
        if len(scores) == 0:
            print("List is empty.")
        else:
            print("Largest Score =", find_largest(scores))

    elif choice == 4:
        if is_sorted(scores):
            print("The scores are sorted in ascending order.")
        else:
            print("The scores are NOT sorted.")

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")