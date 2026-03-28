import tkinter as tk
from tkinter import messagebox

# Function to calculate product
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x200")

# Labels and Entry fields
label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Button to calculate product
calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Product: ")
result_label.pack()

# Run the application
root.mainloop()