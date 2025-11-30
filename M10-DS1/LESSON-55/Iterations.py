from tkinter import *

root = Tk()
root.title("Iteration Example")

text = ""
for i in range(1, 6):   # Iteration loop
    text += str(i) + "\n"

label = Label(root, text=text, font=("Arial", 14))
label.pack(pady=20)

root.mainloop()
