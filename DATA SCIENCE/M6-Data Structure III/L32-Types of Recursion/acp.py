def take_input():
    num = int(input("Enter a number: "))

    if num < 0:
        print("Negative number entered. Program stopped.")
        return
    else:
        take_input()  # Recursive call


# Function call
take_input()