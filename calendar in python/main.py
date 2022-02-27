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
      # Create a GUI window
    new_gui = Tk()
     
    # Set the background colour of GUI window
    new_gui.config(background = "white")
 
    # set the name of tkinter GUI window
    new_gui.title("CALENDAR")
 
    # Set the configuration of GUI window
    new_gui.geometry("550x600")
 
    # get method returns current text as string
    fetch_year = int(entry_y.get())
 
    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)
 
    # Create a label for showing the content of the calendar
    cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.grid(row = 5, column = 1, padx = 20)
     
    # start the GUI
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