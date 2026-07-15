# Flip It with Recursion

# 1. Extract Digits Recursively
def extract_digits(n):
    if n == 0:
        return
    extract_digits(n // 10)
    print(n % 10, end=" ")


# 2. Reverse Number Recursively
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)


# 3. Reverse String Recursively
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]


# 4. Check Power of 4 Recursively
def is_power_of_4(n):
    if n == 1:
        return True
    if n <= 0 or n % 4 != 0:
        return False
    return is_power_of_4(n // 4)


# Main Menu
while True:
    print("\n===== Flip It with Recursion =====")
    print("1. Extract Digits")
    print("2. Reverse Number")
    print("3. Reverse String")
    print("4. Check Power of 4")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        if num == 0:
            print("0")
        else:
            print("Digits:", end=" ")
            extract_digits(num)
            print()

    elif choice == 2:
        num = int(input("Enter a number: "))
        print("Reversed Number:", reverse_number(num))

    elif choice == 3:
        text = input("Enter a string: ")
        print("Reversed String:", reverse_string(text))

    elif choice == 4:
        num = int(input("Enter a number: "))
        if is_power_of_4(num):
            print(num, "is a Power of 4")
        else:
            print(num, "is NOT a Power of 4")

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")