from tkinter import *

root = Tk()

root.geometry("500x200")
root.config(background="light green")

# Functions
def find():
    rank_int = int(entry_r.get())
    total = int(entry_p.get())
    res = round((total - rank_int) / 1000 * 100, 3)
    result.insert(10, res)


def clear():
    entry_r.delete(0, END)
    entry_p.delete(0, END)
    result.delete(0, END)
    entry_r.focus_set()
rank = Label(root, text="Rank", bg="blue", fg="black")
rank.place(x=10, y=10)

entry_r = Entry(root, width=15)
entry_r.focus_set()
entry_r.place(x = 50, y = 12)

and_label = Label(root, text="And", bg="blue", fg="black")
and_label.place(x = 200, y = 10)

participants = Label(root, text="Total Participants", bg="blue", fg="black")
participants.place(x=250, y = 10)

entry_p = Entry(root)
entry_p.place(x = 360, y = 12)

find = Button(root, text="Find Percentile", bg="red", fg="black", command=find)
find.place(x = 200, y = 50)

percentile = Label(root, text="Percentile", bg="blue", fg="black")
percentile.place(x = 100, y = 100)
result = Entry(root)
result.place(x = 180, y = 100)

clear = Button(root, text="Clear", bg="red", fg="black", command=clear)
clear.place(x = 220, y = 130)


root.mainloop()