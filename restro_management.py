from tkinter import *
from datetime import datetime
import pytz
import random

window = Tk()
window.geometry("1200x800")
window.configure(bg="#d98714")
top_frame = Frame(window, width=1000, height=100)
top_frame.pack()
dk= StringVar()
fr= StringVar()
pz = StringVar()
nvb = StringVar()
vb= StringVar()
fc = StringVar()
on = StringVar()
sc= StringVar()
st = StringVar()
tx=StringVar()
t = StringVar()

def result():
  num = random.randint(100000,999999)
  on.set(num)
  d = 0
  f = 0
  p =0
  n =0 
  v = 0
  c = 0
  if dk.get():
    d = float(dk.get())
  if fr.get():
    f = float(fr.get())
  if pz .get():
    p =float(pz.get())
  if nvb.get():
    n = float(nvb.get())
  if vb.get():
   v = float(vb.get())
  if fc.get():
    c = float(fc.get())
  ''' 
  dk_price = 50
  fr_price=100
  pz_price = 250
  nvb_price = 130
  vb_price = 110
  fc_price = 120
  '''
  cod = 50*d
  cof = 100*f
  cop = 250*p
  con = 130*n
  cov = 110*v
  coc = 120*c
  tot = cod+cof+cop+con+cov+coc
  st.set(f"₹{tot}")
  scrv = tot*0.05
  sc.set(f"₹{scrv}")
  txa = tot*0.18
  tx.set(f"₹{txa}")
  tal = tot+scrv+txa
  t.set(f"₹{tal}")
  
def restart():
  dk.set("")
  fr.set("")
  pz.set("")
  nvb.set("")
  vb.set("")
  fc.set("")
  on.set("")
  sc.set("")
  st.set("")
  t.set("")
def remove():
  window.destroy()
def price():
  win = Toplevel()
  win.geometry("200x200")
  win.title("Menu")
  drinks = Label(win,text="Cold Drinks :",font=("Verdana",10,"bold"))
  drinks.grid(row=0,column=0)
  drinks_price = Label(win,text="50",font=("Verdana",10,"bold"))
  drinks_price.grid(row=0,column=1)

  
  french_fries = Label(win,text="French Fries",font=("Verdana",10,"bold"))
  french_fries.grid(row=1,column=0)
  french_price = Label(win,text="100",font=("Verdana",10,"bold"))
  french_price.grid(row=1,column=1)
  
  pizza = Label(win,text="Pizza",font=("Verdana",10,"bold"))
  pizza.grid(row=2,column=0)
  pizza_price = Label(win,text="250",font=("Verdana",10,"bold"))
  pizza_price.grid(row=2,column=1)

  non_veg_burger = Label(win,text="Non Veg Burger",font=("Verdana",10,"bold"))
  non_veg_burger.grid(row=3,column=0)
  non_price = Label(win,text="130",font=("Verdana",10,"bold"))
  non_price.grid(row=3,column=1)

  veg_burger= Label(win,text="Veg Burger",font=("Verdana",10,"bold"))
  veg_burger.grid(row=4,column=0)
  veg_price = Label(win,text="110",font=("Verdana",10,"bold"))
  veg_price.grid(row=4,column=1)

  fried_chicken = Label(win,text="Fried Chicken",font=("Verdana",10,"bold"))
  fried_chicken.grid(row=5,column=0)
  fried_price = Label(win,text="120",font=("Verdana",10,"bold"))
  fried_price.grid(row=5,column=1)
title = Label(top_frame,
              text="Foodie's Restaurant",
              font=("Verdana", 24, "bold"),
              fg="#000000",
              bg="#d98714",
              padx=100)
title.grid(row=0, column=0)
timezone = pytz.timezone("Asia/Kolkata")
dateandtime = datetime.now(timezone)
currenttime = dateandtime.strftime("%d-%m-%Y %H:%M")
l1_time = Label(top_frame,
                text=currenttime,
                font=("Verdana", 18, "bold"),
                fg="#008000",
                bg="#d98714",
                padx=200)
l1_time.grid(row=1, column=0)
bottom_frame = Frame(window, width=1000, height=600, bg="#bdbbb5")
bottom_frame.place(x=250,y=100)
lb_drinks = Label(bottom_frame,
                  text="Cold Drinks",
                  font=("Times", 14, "bold"),
                  fg="#000000",
                  bg="#bdbbb5",
                  pady=10)
lb_drinks.grid(row=0, column=0)
drinks_entry = Entry(bottom_frame, justify="right",textvariable=dk)
drinks_entry.grid(row=0, column=1)

lb_pizza = Label(bottom_frame,
                 text="Pizza",
                 font=("Times", 14, "bold"),
                 fg="#000000",
                 bg="#bdbbb5",
                 pady=10)
lb_pizza.grid(row=1, column=0)
pizza_entry = Entry(bottom_frame, justify="right",textvariable=pz)
pizza_entry.grid(row=1, column=1)

lb_nonveg_burger = Label(bottom_frame,
                         text="Non-Veg Burger",
                         font=("Times", 14, "bold"),
                         fg="#000000",
                         bg="#bdbbb5",
                         pady=10)
lb_nonveg_burger.grid(row=2, column=0)
non_entry = Entry(bottom_frame, justify="right",textvariable=nvb)
non_entry.grid(row=2, column=1)

lb_veg_burger = Label(bottom_frame,
                      text="Veg Burger",
                      font=("Times", 14, "bold"),
                      fg="#000000",
                      bg="#bdbbb5",
                      pady=10)
lb_veg_burger.grid(row=3, column=0)
veg_entry = Entry(bottom_frame, justify="right",textvariable=vb)
veg_entry.grid(row=3, column=1)

lbfries = Label(bottom_frame,
                text="Fries",
                font=("Times", 14, "bold"),
                fg="#000000",
                bg="#bdbbb5",
                pady=10)
lbfries.grid(row=4, column=0)
fries_entry = Entry(bottom_frame, justify="right",textvariable=fr)
fries_entry.grid(row=4, column=1)

lbfried_chicken = Label(bottom_frame,
                        text="Fried Chicken",
                        font=("Times", 14, "bold"),
                        fg="#000000",
                        bg="#bdbbb5",
                        pady=10)
lbfried_chicken.grid(row=5, column=0)
chicken_entry = Entry(bottom_frame, justify="right",textvariable=fc)
chicken_entry.grid(row=5, column=1)



service_charge= Label(bottom_frame,
                    text="Service Charge",
                    font=("Times", 14, "bold"),
                    fg="#000000",
                    bg="#bdbbb5",
                    pady=10)
service_charge.grid(row=0, column=2)
service_entry = Entry(bottom_frame, justify="right",state=DISABLED,textvariable=sc)
service_entry.grid(row=0, column=4)

tax= Label(bottom_frame,
                    text="Tax",
                    font=("Times", 14, "bold"),
                    fg="#000000",
                    bg="#bdbbb5",
                    pady=10)
tax.grid(row=1, column=2)
tax_entry = Entry(bottom_frame, justify="right",state=DISABLED,textvariable=tx)
tax_entry.grid(row=1, column=4)

sub_total = Label(bottom_frame,
                    text="Sub Total",
                    font=("Times", 14, "bold"),
                    fg="#000000",
                    bg="#bdbbb5",
                    pady=10)
sub_total.grid(row=2, column=2)
sub_entry = Entry(bottom_frame, justify="right",state=DISABLED,textvariable=st)
sub_entry.grid(row=2, column=4)
total = Label(bottom_frame,
                    text="Total",
                    font=("Times", 14, "bold"),
                    fg="#000000",
                    bg="#bdbbb5",
                    pady=10)
total.grid(row=3, column=2)
total_entry = Entry(bottom_frame, justify="right",state=DISABLED,textvariable=t)
total_entry.grid(row=3, column=4)

Order_No = Label(bottom_frame,
                    text="Order No",
                    font=("Times", 14, "bold"),
                    fg="#000000",
                    bg="#bdbbb5",
                    pady=10)
Order_No.grid(row=4, column=2)
order_entry = Entry(bottom_frame, justify="right",state=DISABLED,textvariable=on)
order_entry.grid(row=4, column=4)

check=Button(bottom_frame,text="Total",command=result)
check.grid(row=6,column=1)

Reset=Button(bottom_frame,text="Reset",command=restart)
Reset.grid(row=6,column=2)

Quit = Button(bottom_frame,text="Quit",command=remove)
Quit.grid(row=6,column=3)

Menu = Button(bottom_frame,text="Menu Price",command=price)
Menu.grid(row=6,column=4)
window.mainloop()
