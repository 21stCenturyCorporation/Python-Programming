from tkinter import *

root = Tk()
# root.geometry("400x400")
root.resizable(False, False)

# Functions
state = "stop"
def convert():
    global state

    weight = int(entry1.get())
    gram = weight * 1000
    pounds = weight * 2.20462
    ounce = weight * 35.274
    entry2.insert(10, float(gram))
    entry3.insert(10, float(pounds))
    entry4.insert(10, float(ounce))
    state = "start"

    while True:
        if state == "start":    
            weight = int(entry1.get())
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            gram = weight * 1000
            pounds = weight * 2.20462
            ounce = weight * 35.274
            entry2.insert(10, float(gram))
            entry3.insert(10, float(pounds))
            entry4.insert(10, float(ounce))
            state = "stop"
            break
        elif state == "stop":
            weight = int(entry1.get())
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            gram = weight * 1000
            pounds = weight * 2.20462
            ounce = weight * 35.274
            entry2.insert(10, float(gram))
            entry3.insert(10, float(pounds))
            entry4.insert(10, float(ounce))
            state = "start"
            break

empty = Label(root, text=" ")
empty.grid(row=0, column=0)

empty1 = Label(root, text=" ")
empty1.grid(row=0, column=3)

weight_label = Label(root, text="Enter the weight in kg")
weight_label.grid(row=1, column=2)

entry1 = Entry(root)
entry1.grid(row = 1, column=4)

# empty1 = Label(root, text=" ")
# empty1.grid(row=0, column=6)

convert_btn = Button(root, text="Convert", command=convert)
convert_btn.grid(row=1, column=6)

gram = Label(root, text="Gram")
gram.grid(row=2, column=2)

entry2 = Entry(root)
entry2.grid(row=3, column=2)

empty1 = Label(root, text=" ")
empty1.grid(row=2, column=3)

pounds = Label(root, text="Pounds")
pounds.grid(row=2, column=4)

empty1 = Label(root, text=" ")
empty1.grid(row=3, column=3)

entry3 = Entry(root)
entry3.grid(row=3, column=4)

empty1 = Label(root, text=" ")
empty1.grid(row=3, column=5)

ounce = Label(root, text="Ounce")
ounce.grid(row=2, column=6)

# empty1 = Label(root, text=" ")
# empty1.grid(row=3, column=6)

entry4 = Entry(root)
entry4.grid(row=3, column=6)



root.mainloop()