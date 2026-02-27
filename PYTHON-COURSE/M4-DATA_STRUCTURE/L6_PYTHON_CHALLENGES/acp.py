import random
import string

def generate_password(length):
    """
    Generate a random password containing lowercase, uppercase letters and numbers.

    Parameters:
        length (int): Length of the password (minimum 3 recommended)
    
    Returns:
        str: Randomly generated password
    """
    if length < 3:
        return "Password length should be at least 3"

    # Characters to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Ensure the password has at least one lowercase, one uppercase, and one digit
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    # Fill the rest of the password length with random choices from all characters
    all_chars = lowercase + uppercase + digits
    password += [random.choice(all_chars) for _ in range(length - 3)]

    # Shuffle the password list to make it random
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)


# Example usage
length = int(input("Enter the desired password length: "))
password = generate_password(length)
print("Randomly generated password:", password)