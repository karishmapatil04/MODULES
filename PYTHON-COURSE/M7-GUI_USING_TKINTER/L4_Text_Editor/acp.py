import tkinter as tk
from tkinter import messagebox

# Function to calculate SI and CI
def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Simple Interest
        si = (principal * rate * time) / 100

        # Compound Interest (annual compounding)
        amount = principal * (1 + rate / 100) ** time
        ci = amount - principal

        result_label.config(
            text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values")

# Create main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x250")

# Labels and Entry fields
tk.Label(root, text="Enter Principal Amount:").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Enter Rate of Interest (%):").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Enter Time (years):").pack()
entry_time = tk.Entry(root)
entry_time.pack()

# Button to calculate interest
tk.Button(root, text="Calculate Interest", command=calculate_interest).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Results will appear here")
result_label.pack()

# Run the application
root.mainloop()