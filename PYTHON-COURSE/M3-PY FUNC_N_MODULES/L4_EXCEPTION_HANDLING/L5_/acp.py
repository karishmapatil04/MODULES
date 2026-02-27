def check_age(age):
    """
    Checks if the age is valid and determines if it is even or odd.
    
    Parameters:
        age (int): Age entered by the user
    
    Returns:
        str: Result message
    """
    if age < 0 or age > 120:
        return "Error: Age entered is not valid."
    
    if age % 2 == 0:
        return "Age is valid and it is Even."
    else:
        return "Age is valid and it is Odd."


# Main program
try:
    user_input = int(input("Enter your age: "))
    result = check_age(user_input)
    print(result)
except ValueError:
    print("Error: Please enter a valid integer for age.")