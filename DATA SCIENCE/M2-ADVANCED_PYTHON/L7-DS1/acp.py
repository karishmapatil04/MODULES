import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    # List to store all guesses (data structure used)
    guesses = []
    
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100")

    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses.append(guess)  # storing guess in list
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

    print("\nYour guesses were:", guesses)

# Run the game
number_guessing_game()