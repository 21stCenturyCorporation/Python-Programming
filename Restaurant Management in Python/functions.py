from tkinter import *
import sys

def price():
    new_window = Tk()

    new_window.geometry("500x400")

    lbl_item = Label(new_window, text="ITEM", font=("Ariel", 20, "bold"))
    lbl_item.grid(row=0, column=0, padx=30, pady=10)

    fries = Label(new_window, text="Fries Meal", font=("Ariel", 15, "bold"), fg="steel blue")
    fries.grid(row=1, column=0, padx=30, pady=10)

    lunch_meal = Label(new_window, text="Lunch Meal", font=("Ariel", 15, "bold"), fg="steel blue")
    lunch_meal.grid(row=2, column=0, padx=30, pady=10)

    burger_meal = Label(new_window, text="Burger Meal", font=("Ariel", 15, "bold"), fg="steel blue")
    burger_meal.grid(row=3, column=0, padx=30, pady=10)

    pizza_meal = Label(new_window, text="Pizza Meal", font=("Ariel", 15, "bold"), fg="steel blue")
    pizza_meal.grid(row=4, column=0, padx=30, pady=10)

    cheese_burger = Label(new_window, text="Cheese Burger", font=("Ariel", 15, "bold"), fg="steel blue")
    cheese_burger.grid(row=5, column=0, padx=30, pady=10)


    drinks = Label(new_window, text="Drinks", font=("Ariel", 15, "bold"), fg="steel blue")
    drinks.grid(row=6, column=0, padx=30, pady=10)

    price_list = Label(new_window, text="Price", font=("Ariel", 15, "bold"))
    price_list.grid(row=0, column=1, padx=10, pady=10)

    p1 = Label(new_window, text="25", font=("Ariel", 15, "bold"), fg="steel blue")
    p1.grid(row=1, column=1, padx=30, pady=10)

    p2 = Label(new_window, text="40", font=("Ariel", 15, "bold"), fg="steel blue")
    p2.grid(row=2, column=1, padx=30, pady=10)

    p3 = Label(new_window, text="35", font=("Ariel", 15, "bold"), fg="steel blue")
    p3.grid(row=3, column=1, padx=30, pady=10)

    p4 = Label(new_window, text="50", font=("Ariel", 15, "bold"), fg="steel blue")
    p4.grid(row=4, column=1, padx=30, pady=10)

    p5 = Label(new_window, text="30", font=("Ariel", 15, "bold"), fg="steel blue")
    p5.grid(row=5, column=1, padx=30, pady=10)

    p6 = Label(new_window, text="35", font=("Ariel", 15, "bold"), fg="steel blue")
    p6.grid(row=6, column=1, padx=30, pady=10)

    new_window.mainloop()


def exit_app():
    sys.exit()

