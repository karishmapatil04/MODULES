import tkinter as tk
from tkinter import messagebox
from datetime import date

# Function to calculate age
def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        birth_date = date(year, month, day)
        today = date.today()

        age = today.year - birth_date.year

        # Adjust age if birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Present Age: {age} years")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid date values")

# Create main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x250")

# Labels and Entry fields
tk.Label(root, text="Enter Day (DD):").pack()
entry_day = tk.Entry(root)
entry_day.pack()

tk.Label(root, text="Enter Month (MM):").pack()
entry_month = tk.Entry(root)
entry_month.pack()

tk.Label(root, text="Enter Year (YYYY):").pack()
entry_year = tk.Entry(root)
entry_year.pack()

# Button to calculate age
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Present Age: ")
result_label.pack()

# Run the application
root.mainloop()