# Keypad Word Generator

# Phone keypad mapping
keypad = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}

# 1. Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move Disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move Disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# 2. Generate Keypad Words
def keypad_words(digits, current, index):
    if index == len(digits):
        print(current)
        return

    letters = keypad.get(digits[index], "")

    for ch in letters:
        keypad_words(digits, current + ch, index + 1)


# 3. Trace Keypad Recursion Tree
def trace_keypad(digits, current, index):
    print("Call ->", current)

    if index == len(digits):
        print("Word:", current)
        return

    letters = keypad.get(digits[index], "")

    for ch in letters:
        trace_keypad(digits, current + ch, index + 1)


# Main Menu
while True:
    print("\n===== Keypad Word Generator =====")
    print("1. Tower of Hanoi")
    print("2. Generate Keypad Words")
    print("3. Trace Keypad Recursion")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of disks: "))
        tower_of_hanoi(n, "A", "B", "C")

    elif choice == 2:
        digits = input("Enter digits (2-9): ")
        print("Possible Words:")
        keypad_words(digits, "", 0)

    elif choice == 3:
        digits = input("Enter digits (2-9): ")
        print("Recursion Trace:")
        trace_keypad(digits, "", 0)

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")