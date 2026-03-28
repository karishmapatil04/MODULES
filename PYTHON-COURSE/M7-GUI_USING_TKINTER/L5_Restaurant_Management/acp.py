import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    )

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Title label
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12)).pack(pady=10)

# Buttons
tk.Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=20)

# Run the application
root.mainloop()