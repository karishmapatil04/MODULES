import random
import string

# Function to generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

# Main program
length = int(input("Enter password length: "))
password = generate_password(length)

print("Generated Password:", password)