import random
import tkinter as tk

# Function to play game
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    # Game logic using conditional statements
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Display result
    result_label.config(
        text=f"You: {user_choice}\nComputer: {computer_choice}\nResult: {result}"
    )

# Create GUI window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

# Heading
heading = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 14))
heading.pack(pady=10)

# Buttons for choices
btn_rock = tk.Button(root, text="Rock", width=12, command=lambda: play("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=12, command=lambda: play("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=12, command=lambda: play("Scissors"))
btn_scissors.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

# Run loop
root.mainloop()