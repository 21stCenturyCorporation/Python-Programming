from tkinter import *
import sqlite3
from tkinter import messagebox


def add():

    conn = sqlite3.connect("C:\\Users\\21st Century\\Desktop\\desktop important\\Python Tutorial\\Library Management System\\database.db")

    cursor = conn.cursor()

    global entry1, entry2, entry3, entry4, entry5
    name = entry1.get()
    price = entry2.get()
    category = entry3.get()
    description = entry4.get()
    quantity = entry5.get()

    sql = f"insert into Library(Name, Price, Category, Description, Quantity) values('{name}', '{price}', '{category}', '{description}', '{quantity}')"
    
    cursor.execute(sql)

    conn.commit()

    conn.close()

def view():
    wn = Tk()
    wn.title("View Data")

    conn = sqlite3.connect("C:\\Users\\21st Century\\Desktop\\desktop important\\Python Tutorial\\Library Management System\\database.db")

    cursor = conn.cursor()

    sql = "select Name, Price, Category, Description, Quantity from Library"
    data = cursor.execute(sql)


    # Labels
    label1 = Label(wn, text="Book Name")
    label2 = Label(wn, text="Price")
    label3 = Label(wn, text="Category")
    label4 = Label(wn, text="Description")
    label5 = Label(wn, text="Quantity")

    # Gridding the labels
    label1.grid(row=0, column=0, padx=10, pady=10)
    label2.grid(row=0, column=1, padx=10, pady=10)
    label3.grid(row=0, column=2, padx=10, pady=10)
    label4.grid(row=0, column=3, padx=10, pady=10)
    label5.grid(row=0, column=4, padx=10, pady=10)
    i = 1
    j = 0
    for record in data:
        name = Label(wn, text=str(record[0]))
        price = Label(wn, text=str(record[1]))
        category = Label(wn, text=str(record[2]))
        description = Label(wn, text=str(record[3]))
        quantity = Label(wn, text=str(record[4]))

        name.grid(row=i, column=j)
        price.grid(row=i, column=j+1)
        category.grid(row=i, column=j+2)
        description.grid(row=i, column=j+3)
        quantity.grid(row=i, column=j+4)

        i += 1
        
    conn.close()


    wn.mainloop()

def delete_data():
    global entry_id
    conn = sqlite3.connect("C:\\Users\\21st Century\\Desktop\\desktop important\\Python Tutorial\\Library Management System\\database.db")

    cursor = conn.cursor()

    sql = "DELETE from Library WHERE id="+entry_id.get()
    
    cursor.execute(sql)

    conn.commit()


def delete():
    global entry_id
    win = Tk()
    win.title("Delete Data")

    id = IntVar()

    entry_id = Entry(win, textvariable=id)
    entry_id.grid(row=0, column=0, padx=10, pady=10)

    delete_btn = Button(win, text="Delete Record", command=delete_data)
    delete_btn.grid(row=1, column=0, padx=10, pady=10, rowspan=7)

    win.mainloop()


def exit_app():
    global root
    root.destroy()

def main():
    global entry1, entry2, entry3, entry4, entry5, root
    root = Tk()
    root.title("Library Management System")

    # Labels
    label1 = Label(root, text="Book Name")
    label2 = Label(root, text="Price")
    label3 = Label(root, text="Category")
    label4 = Label(root, text="Description")
    label5 = Label(root, text="Quantity")

    # Gridding the labels
    label1.grid(row=0, column=0, padx=10, pady=10)
    label2.grid(row=1, column=0, padx=10, pady=10)
    label3.grid(row=2, column=0, padx=10, pady=10)
    label4.grid(row=3, column=0, padx=10, pady=10)
    label5.grid(row=4, column=0, padx=10, pady=10)

    # Entries
    entry1 = Entry(root)
    entry2 = Entry(root)
    entry3 = Entry(root)
    entry4 = Entry(root)
    entry5 = Entry(root)

    # Gridding the entries
    entry1.grid(row=0, column=1, padx=10, pady=10)
    entry2.grid(row=1, column=1, padx=10, pady=10)
    entry3.grid(row=2, column=1, padx=10, pady=10)
    entry4.grid(row=3, column=1, padx=10, pady=10)
    entry5.grid(row=4, column=1, padx=10, pady=10)

    # Buttons
    btn_add = Button(root, text="Add Data", command=add)
    btn_delete = Button(root, text="Delete Data", command=delete)
    btn_view = Button(root, text="View Data", command=view)
    btn_exit = Button(root, text="Exit Application", command=exit_app)

    # Gridding the buttons
    btn_add.grid(row=5, column=0, padx=10, pady=10)
    btn_delete.grid(row=5, column=1, padx=10, pady=10)
    btn_view.grid(row=6, column=0, padx=10, pady=10)
    btn_exit.grid(row=6, column=1, padx=10, pady=10)

    root.mainloop()

def login():
    global user, pass_word, username, password
    if user.get() == username and pass_word.get() == password:
        main()
    else:
        messagebox.showerror("Library Management System", "Wrong Username or Password. Please try again")

window = Tk()
window.title("Login Form")

user = StringVar()
pass_word = StringVar()
username = "nil"
password = "nil"

label1 = Label(window, text="Username")
label2 = Label(window, text="Password")

label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)

en1 = Entry(window, textvariable=user)
en2 = Entry(window, textvariable=pass_word)

en1.grid(row=0, column=1, padx=10, pady=10)
en2.grid(row=1, column=1, padx=10, pady=10)

btn_login = Button(window, text="Login", command=login)
btn_login.grid(row=2, column=0, padx=10, pady=10, columnspan=9)



window.mainloop()
