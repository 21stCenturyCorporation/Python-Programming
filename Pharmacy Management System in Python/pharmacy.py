from tkinter import *
import sqlite3

root = Tk()
root.title("Pharmacy Management System in Python")

# Functions


def delete_data():
    global entry_id
    conn = sqlite3.connect("pharmacy.db")

    cursor = conn.cursor()

    sql = "DELETE from pharmacy WHERE id=" + entry_id.get()

    cursor.execute(sql)

    conn.commit()


def delete():
    global entry_id
    wn = Tk()

    id = IntVar()

    label = Label(wn, text="Enter the index to be deleted")
    label.grid(row=0, column=0, padx=10, pady=10)

    entry_id = Entry(wn, textvariable=id)
    entry_id.grid(row=0, column=1, padx=10, pady=10)

    button_delete = Button(wn, text="Delete", command=delete_data)
    button_delete.grid(row=1, column=0, padx=10, pady=10, rowspan=7)
    wn.mainloop()


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry1.focus_set()


def add():
    conn = sqlite3.connect("pharmacy.db")

    cursor = conn.cursor()

    name = entry1.get()
    price = entry2.get()
    category = entry3.get()
    description = entry4.get()
    quantity = entry5.get()
    sql = f"insert into pharmacy(Name, Price, Category, Description, Quantity) values('{name}', '{price}', '{category}', '{description}', '{quantity}')"
    cursor.execute(sql)
    conn.commit()
    conn.close()
    clear()


def exit_app():
    root.destroy()


def view():
    conn = sqlite3.connect("pharmacy.db")

    cursor = conn.cursor()

    sql = "select Name, Price, Category, Description, Quantity from pharmacy"
    data = cursor.execute(sql)

    window = Tk()
    window.title("View Data")

    label_1 = Label(window, text="Medicine Name")
    label_2 = Label(window, text="Medicine Price")
    label_3 = Label(window, text="Medicine Category")
    label_4 = Label(window, text="Medicine Description")
    label_5 = Label(window, text="Medicine Quantity")

    label_1.grid(row=0, column=0, padx=10, pady=10)
    label_2.grid(row=0, column=1, padx=10, pady=10)
    label_3.grid(row=0, column=2, padx=10, pady=10)
    label_4.grid(row=0, column=3, padx=10, pady=10)
    label_5.grid(row=0, column=4, padx=10, pady=10)

    i = 1
    j = 0

    for record in data:
        name = Label(window, text=str(record[0]))
        price = Label(window, text=str(record[1]))
        category = Label(window, text=str(record[2]))
        description = Label(window, text=str(record[3]))
        quantity = Label(window, text=str(record[4]))

        # Griding the labels
        name.grid(row=i, column=j)
        price.grid(row=i, column=j+1)
        category.grid(row=i, column=j+2)
        description.grid(row=i, column=j+3)
        quantity.grid(row=i, column=j+4)

        i += 1

    window.mainloop()


# Creating the labels
label1 = Label(root, text="Medicine Name")
label2 = Label(root, text="Medicine Price")
label3 = Label(root, text="Medicine Category")
label4 = Label(root, text="Medicine Description")
label5 = Label(root, text="Medicine Quantity")

# Griding the labels
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
label3.grid(row=2, column=0, padx=10, pady=10)
label4.grid(row=3, column=0, padx=10, pady=10)
label5.grid(row=4, column=0, padx=10, pady=10)

# Creating the entries
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)

# Griding the Entries
entry1.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
entry3.grid(row=2, column=1, padx=10, pady=10)
entry4.grid(row=3, column=1, padx=10, pady=10)
entry5.grid(row=4, column=1, padx=10, pady=10)

# Creating the buttons
btn_add = Button(root, text="Add Data", command=add)
btn_delete = Button(root, text="Delete Data", command=delete)
btn_view = Button(root, text="View Data", command=view)
btn_exit = Button(root, text="Exit Application", command=exit_app)

# Griding the buttons
btn_add.grid(row=5, column=0, padx=10, pady=10)
btn_delete.grid(row=5, column=1, padx=10, pady=10)
btn_view.grid(row=6, column=0, padx=10, pady=10)
btn_exit.grid(row=6, column=1, padx=10, pady=10)


root.mainloop()
