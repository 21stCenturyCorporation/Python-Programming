from tkinter import *
import sys
from tkinter import filedialog

root = Tk()
root.resizable(False, False)
root.geometry("500x500")
root.config(background="white")

# Functions

def explore():
    files = filedialog.askopenfilename(initialdir="/", title="Select Files", filetypes=(("Text Document", ".txt"), ("All files", ".")))

    file_explorer["text"] = files

def exit():
    sys.exit()

file_explorer = Label(root, text="File explorer using Tkinter", width=71, height=4, fg="blue")
file_explorer.grid(row=1, column=1)

btn_browse = Button(root, text="Browse Files", command=explore)
btn_browse.grid(row=2, column=1)

btn_exit = Button(root, text="Exit", command=exit)
btn_exit.grid(row=3, column=1)

root.mainloop()