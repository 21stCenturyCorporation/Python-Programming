from tkinter import *
import time
import random
from functions import price, exit_app

root = Tk()
root.state("zoom")
root.geometry("1024x768+0+0")

# functions
def total_price():
    random_value = random.randint(1000, 5000)
    e1.delete(0, END)
    e1.insert(10, random_value)
    
    # Get all the inputs of the user
    fries = int(e2.get())
    lunch = int(e3.get())
    burger = int(e4.get())
    pizza = int(e5.get())
    cheese_burger = int(e6.get())
    drinks = int(e7.get())

    # Calculating all the values
    cost = fries * 25 + lunch * 40 + burger * 35 + pizza * 50 + cheese_burger * 30 + drinks * 35
    
    sub_total_val = cost

    service_charge = round(cost / 99, 2)

    tax = round(cost * 0.33, 2)

    total = round(cost + service_charge + tax, 3)

    # Inserting the values

    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)

    e8.insert(10, cost)
    e9.insert(10, service_charge)
    e10.insert(10, tax)
    e11.insert(10, sub_total_val)
    e12.insert(10, total)


def reset(entry,*args, **kwargs):
    for i in entry:
        i.delete(0, END)
    e2.focus_set()
# Designing

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)


label = Label(Tops, text="Restuarant Management System in Python", font=("aria", 30, "bold"),fg="steel blue", bd=10)
label.grid(row=0, column=0)

local_time = time.asctime(time.localtime(time.time()))

lbl_time = Label(Tops, font=( 'aria' ,20, "normal"),text=local_time,fg="steel blue",anchor=W)
lbl_time.grid(row=1,column=0)

order_no = Label(f1, text="Order No.", font=("aria", 15, "bold"), fg="steel blue")
order_no.grid(row=2, column=0, padx=20, pady=20)

fries_meal = Label(f1, text="Fries Meal", font=("aria", 15, "bold"), fg="steel blue")
fries_meal.grid(row=3, column=0, padx=20, pady=20)

lunch_meal = Label(f1, text="Lunch Meal", font=("aria", 15, "bold"), fg="steel blue")
lunch_meal.grid(row=4, column=0, padx=20, pady=20)

burger_meal = Label(f1, text="Burger Meal", font=("aria", 15, "bold"), fg="steel blue")
burger_meal.grid(row=5, column=0, padx=20, pady=20)

pizza_meal = Label(f1, text="Pizza Meal", font=("aria", 15, "bold"), fg="steel blue")
pizza_meal.grid(row=6, column=0, padx=20, pady=20)

cheese_burger = Label(f1, text="Cheese Burger", font=("aria", 15, "bold"), fg="steel blue")
cheese_burger.grid(row=7, column=0, padx=20, pady=20)

drinks = Label(f1, text="Drinks", font=("aria", 15, "bold"), fg="steel blue")
drinks.grid(row=2, column=2, padx=20, pady=20)

cost = Label(f1, text="Cost", font=("aria", 15, "bold"), fg="steel blue")
cost.grid(row=3, column=2, padx=20, pady=20)

service_charge = Label(f1, text="Service Charge", font=("aria", 15, "bold"), fg="steel blue")
service_charge.grid(row=4, column=2, padx=20, pady=20)

tax = Label(f1, text="Tax", font=("aria", 15, "bold"), fg="steel blue")
tax.grid(row=5, column=2, padx=20, pady=20)

sub_total = Label(f1, text="Sub Total", font=("aria", 15, "bold"), fg="steel blue")
sub_total.grid(row=6, column=2, padx=20, pady=20)

total = Label(f1, text="Total", font=("aria", 15, "bold"), fg="steel blue")
total.grid(row=7, column=2, padx=10, pady=20)

# Entries
e1 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e2 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e2.focus_set()
e3 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e4 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e5 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e6 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e7 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e8 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e9 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e10 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e11 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))
e12 = Entry(f1, bd=6,bg="powder blue" ,justify='right', font=("Montserrat", 15, "bold"))

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)
e4.grid(row=5, column=1)
e5.grid(row=6, column=1)
e6.grid(row=7, column=1)
e7.grid(row=2, column=3)
e8.grid(row=3, column=3)
e9.grid(row=4, column=3)
e10.grid(row=5, column=3)
e11.grid(row=6, column=3)
e12.grid(row=7, column=3)

# Buttons
btn_price=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue", command=price)
btn_price.grid(row=8, column=0, padx=10)

btn_total = Button(f1, padx=16, pady=8, bd=10, fg="black", font=("Ariel", 16, "bold"), width=10, text="TOTAL", bg="powder blue", command=total_price)
btn_total.grid(row=8, column=1, padx=10)

btn_reset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=("Ariel", 16, "bold"), width=10, text="RESET", bg="powder blue", command=lambda: reset([e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12]) )
btn_reset.grid(row=8, column=2, padx=10)

btn_exit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=("Ariel", 16, "bold"), width=10, text="EXIT", bg="powder blue", command=exit_app)
btn_exit.grid(row=8, column=3, padx=10)


root.mainloop()