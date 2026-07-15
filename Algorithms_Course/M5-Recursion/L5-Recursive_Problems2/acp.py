# Stair Climb and Brace Builder

# 1. Count Ways to Climb Stairs
def stair_climb(n):
    if n == 0 or n == 1:
        return 1
    return stair_climb(n - 1) + stair_climb(n - 2)


# 2. Trace Recursive Call Tree
def trace_stairs(n):
    print("Call -> stair(", n, ")")

    if n == 0 or n == 1:
        print("Return <- 1")
        return 1

    left = trace_stairs(n - 1)
    right = trace_stairs(n - 2)

    result = left + right
    print("Return <-", result)
    return result


# 3. Generate Balanced Braces
def generate_braces(open_brace, close_brace, current):
    if open_brace == 0 and close_brace == 0:
        print(current)
        return

    if open_brace > 0:
        generate_braces(open_brace - 1, close_brace, current + "{")

    if close_brace > open_brace:
        generate_braces(open_brace, close_brace - 1, current + "}")


# Main Menu
while True:
    print("\n===== Stair Climb and Brace Builder =====")
    print("1. Count Stair Climbing Ways")
    print("2. Trace Stair Call Tree")
    print("3. Generate Balanced Braces")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of stairs: "))
        print("Number of ways =", stair_climb(n))

    elif choice == 2:
        n = int(input("Enter number of stairs: "))
        print("Tracing Recursive Calls:")
        ways = trace_stairs(n)
        print("Total Ways =", ways)

    elif choice == 3:
        n = int(input("Enter number of brace pairs: "))
        print("Balanced Brace Combinations:")
        generate_braces(n, n, "")

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")