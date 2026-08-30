valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        valid = True
    except ValueError:
        print("Invalid")