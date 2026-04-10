import random
import tkinter as tk

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

    result_var.set(f"You: {user_choice} | Computer: {computer_choice}\nResult: {result}")

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Arial", 12))
label.pack(pady=10)

# Buttons
btn_rock = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_scissors.pack(pady=5)

# Result display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, fg="blue", font=("Arial", 11))
result_label.pack(pady=20)

# Run GUI loop
root.mainloop()