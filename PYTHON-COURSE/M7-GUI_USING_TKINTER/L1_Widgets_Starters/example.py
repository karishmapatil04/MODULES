from tkinter import *

window = Tk()
window.title('Demo Window')
window.geometry('400x300')

lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=100)
lbl.pack()

name_entry = Entry()
name_entry.pack()
name = name_entry.get()  # inside display()


window.mainloop()