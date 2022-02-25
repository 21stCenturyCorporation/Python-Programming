import sys
from tkinter import *
import calendar

root = Tk()
root.resizable(False, False)
root.geometry("200x200")

# functions
def exit():
    sys.exit()


def show():
    new_gui = Tk()

    new_gui.geometry("550x620")
    new_gui.resizable(False, False)
    new_gui.config(background="white")
    fetch_year = int(entry_y.get())
    show_year = calendar.calendar(fetch_year)

    area = Label(new_gui, text=show_year, bg="light gray", fg="black", font=("Montserrat", 9, 'bold'))
    area.focus_set()
    area.place(x = 30, y=10)

    new_gui.mainloop()


year = Label(root, text="Enter year", font=("Montserrat", 10, "bold"),bg="light green", fg="black")
year.place(x=50, y=50)

entry_y = Entry(root)
entry_y.focus_set()
entry_y.place(x = 30, y = 80)

show = Button(root, text="Show Calendar", bg="red", fg="black", font=("Montserrat", 12, "bold"), command=show)
show.place(x = 20, y = 110)

exit = Button(root, text="Exit Calendar", bg="red", fg="black", font=("Montserrat", 10, "bold"), command=exit)
exit.place(x = 35, y = 160)

root.mainloop()