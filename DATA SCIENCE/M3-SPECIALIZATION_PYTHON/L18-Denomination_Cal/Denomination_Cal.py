from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Image
upload = Image.open(r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\DATA SCIENCE\M3-SPECIALIZATION_PYTHON\L18-Denomination_Cal\chicago.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function for message
def msg():
    messagebox.showinfo("Alert", "Proceeding to denomination counter")
    topwin()

# Button
button1 = Button(root,
    text="Let's get started!",
    command=msg,
    bg='brown',
    fg='white')
button1.place(x=260, y=360)

# Top Window Function
def topwin():
    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('600x400')

    # Widgets inside top window
    lbl = Label(top, text="Enter Amount:", bg='grey')
    lbl.place(x=200, y=50)

    entry = Entry(top)
    entry.place(x=200, y=80)

    def calculate():
        amount = int(entry.get())
        note100 = amount // 100
        amount %= 100

        note50 = amount // 50
        amount %= 50

        note10 = amount // 10

        t1.config(text=str(note100))
        t2.config(text=str(note50))
        t3.config(text=str(note10))

    btn = Button(top, text="Calculate", command=calculate)
    btn.place(x=230, y=120)

    l1 = Label(top, text="100 Notes:", bg='grey')
    l1.place(x=180, y=200)

    l2 = Label(top, text="50 Notes:", bg='grey')
    l2.place(x=180, y=230)

    l3 = Label(top, text="10 Notes:", bg='grey')
    l3.place(x=180, y=260)

    t1 = Label(top, text="", bg='grey')
    t1.place(x=300, y=200)

    t2 = Label(top, text="", bg='grey')
    t2.place(x=300, y=230)

    t3 = Label(top, text="", bg='grey')
    t3.place(x=300, y=260)

root.mainloop()