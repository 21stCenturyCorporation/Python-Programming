from tkinter import *
from tkinter import messagebox
from random import *

root = Tk()
root.geometry("277x310")

# Your path to database.txt
dir = "database.txt"

# Functions
def clear_list_box():
    lists.delete(0, "end")

def update_tasks():
    clear_list_box()
    for task in tasks:
        lists.insert("end", task)

def add_data():
    label_display['text'] = ''
    data = entry.get()
    if data != "":
        tasks.append(data)
        update_tasks()
        
    else:
        messagebox.showerror("Todo's App", "Please enter your todo in the entry")
    entry.delete(0, END)
    
def delete():
    active = lists.get("active")
    if active in tasks:
        tasks.remove(active)
    update_tasks()

def delete_all():
    conf = messagebox.askquestion(
        'delet all??', 'are you sure to delete all task?')
    if conf.upper() == "YES":
        global tasks
        tasks = []
        update_tasks()
    else:
        pass

def sort_asc():
    tasks.sort()
    update_tasks()

def sort_dsc():
    tasks.sort(reverse=True)
    update_tasks()

def random_task():
    if (len(tasks) > 0):
        random_task = choice(tasks)
        label_display['text'] = random_task
    else:
        messagebox.showerror("Todo's App", "Sorry no tasks available. Please enter a task or load tasks")

def number_tasks():
    if (len(tasks) > 0):
        label_display["text"] = len(tasks)
    else:
        messagebox.showerror("Todo's App", "Sorry no tasks available. Please enter a task or load tasks")

def exit():
    root.destroy()

def load_list():
    conf = messagebox.askquestion("Todo's App", "Have you saved your progress? If no, then click on the No button")
    
    if conf.upper() == "YES":
        tasks.clear()
        db = open(dir, 'r')

        for data in db:
            tasks.append(data)
        update_tasks()

def save_list():
    save = messagebox.askquestion(
        'Save Confirmation', 'save your progress?')
    if save.upper() == "YES":
        with open(dir, "w") as filehandle:
            for task in tasks:
                filehandle.write('%s\n' % task)
    else:
        pass

def info():
    messagebox.showinfo("Todo's App", "21st Century Todo's App. This application is an opensource project which is just a solution of a test. This application is programmed by Nillohit Roy. You can also contribute your code in github.")

tasks = []  

label = Label(root, text="Todo List")
label.grid(row=0, column=0, padx=30)

label_display = Label(root, text="")
label_display.grid(row=0, column=1, padx=10)
entry = Entry(root)
entry.grid(row=1, column=1, padx=10)

lists = Listbox(root)
lists.grid(row=2, column=1, rowspan=7)

btn_add = Button(root, text="Add Todo", height=1, width=12, padx=10, command=add_data)
btn_add.grid(row=1, column=0)

btn_done = Button(root, text="Done Task", height=1, width=12, padx=10, command=delete)
btn_done.grid(row=2, column=0)

btn_delete= Button(root, text="Delete All", height=1, width=12, padx=10, command=delete_all)
btn_delete.grid(row=3, column=0)

btn_sort_asc = Button(root, text="Sort (ASC)", height=1, width=12, padx=10, command=sort_asc)
btn_sort_asc.grid(row=4, column=0)

btn_sort_dsc = Button(root, text="Sort (DSC)", height=1, width=12, padx=10, command=sort_dsc)
btn_sort_dsc.grid(row=5, column=0)

btn_random = Button(root, text="Random Task", height=1, width=12, padx=10, command=random_task)
btn_random.grid(row=6, column=0)

btn_number = Button(root, text="Number of Tasks", height=1, width=12, padx=10, command=number_tasks)
btn_number.grid(row=7, column=0)

btn_exit = Button(root, text="Exit App", height=1, width=12, padx=10, command=exit)
btn_exit.grid(row=8, column=0)

btn_load = Button(root, text="Load Todolist", height=1, width=12, padx=10, command=load_list)
btn_load.grid(row=9, column=0)

btn_save = Button(root, text="Save Todolist", height=1, width=12, padx=10, command=save_list)
btn_save.grid(row=9, column=1, padx=5)

btn_info = Button(root, text="Info", height=1, width=12, padx=10)
btn_info.grid(row=10, column=0, columnspan=5, pady=5)

root.mainloop()