import tkinter as tk

# Function to check password strength
def check_strength():
    password = entry_password.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password")
    elif length < 6:
        result_label.config(text="Strength: Weak")
    elif 6 <= length < 10:
        result_label.config(text="Strength: Medium")
    else:
        result_label.config(text="Strength: Strong")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

# Label and Entry field
tk.Label(root, text="Enter Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Button to check strength
tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Strength: ")
result_label.pack(pady=5)

# Run the application
root.mainloop()