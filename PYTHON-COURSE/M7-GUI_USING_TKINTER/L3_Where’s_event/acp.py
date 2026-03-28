import tkinter as tk
from tkinter import messagebox

# Function to convert inches to centimeters
def convert_length():
    try:
        inches = float(entry_inches.get())
        centimeters = inches * 2.54
        result_label.config(text=f"Length in cm: {centimeters:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Create main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("320x200")

# Label and Entry field
tk.Label(root, text="Enter length in inches:").pack(pady=5)
entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)

# Convert button
tk.Button(root, text="Convert", command=convert_length).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Length in cm: ")
result_label.pack(pady=5)

# Run the application
root.mainloop()