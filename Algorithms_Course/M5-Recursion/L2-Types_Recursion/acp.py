# Stack Frame Visualizer

# 1. Linear Recursion
def linear_recursion(n):
    print("Call -> linear(", n, ")")
    if n == 0:
        print("Return <- linear(", n, ")")
        return
    linear_recursion(n - 1)
    print("Return <- linear(", n, ")")


# 2. Tail Recursion
def tail_recursion(n):
    print("Call -> tail(", n, ")")
    if n == 0:
        print("Return <- tail(", n, ")")
        return
    print("Processing:", n)
    tail_recursion(n - 1)
    print("Return <- tail(", n, ")")


# 3. Head Recursion
def head_recursion(n):
    print("Call -> head(", n, ")")
    if n == 0:
        print("Return <- head(", n, ")")
        return
    head_recursion(n - 1)
    print("Processing:", n)
    print("Return <- head(", n, ")")


# 4. Increasing-Decreasing Recursion
def inc_dec_recursion(n):
    print("Call -> inc_dec(", n, ")")
    if n == 0:
        print("Return <- inc_dec(", n, ")")
        return
    print("Increasing:", n)
    inc_dec_recursion(n - 1)
    print("Decreasing:", n)
    print("Return <- inc_dec(", n, ")")


# 5. Tree Recursion
def tree_recursion(n):
    print("Call -> tree(", n, ")")
    if n == 0:
        print("Return <- tree(", n, ")")
        return
    tree_recursion(n - 1)
    tree_recursion(n - 1)
    print("Return <- tree(", n, ")")


# Main Menu
while True:
    print("\n===== Stack Frame Visualizer =====")
    print("1. Linear Recursion")
    print("2. Tail Recursion")
    print("3. Head Recursion")
    print("4. Increasing-Decreasing Recursion")
    print("5. Tree Recursion")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Program Ended.")
        break

    n = int(input("Enter value of n: "))

    if choice == 1:
        linear_recursion(n)

    elif choice == 2:
        tail_recursion(n)

    elif choice == 3:
        head_recursion(n)

    elif choice == 4:
        inc_dec_recursion(n)

    elif choice == 5:
        tree_recursion(n)

    else:
        print("Invalid Choice!")