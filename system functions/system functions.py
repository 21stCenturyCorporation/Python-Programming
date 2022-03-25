import os
from tkinter import *
from tkinter import ttk

root = Tk()
root.resizable(False, False)
root.title("System Functions in Python")
style = ttk.Style(root)

# Functions
def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def logout():
    os.system("shutdown -l")

btn_shutdown = ttk.Button(root, text="Shutdown", command=shutdown)
btn_shutdown.grid(row=0, column=0, padx=50, pady=10)

btn_restart = ttk.Button(root, text="Restart", command=restart)
btn_restart.grid(row=1, column=0, padx=50, pady=10)

btn_logout = ttk.Button(root, text="Logout", command=logout)
btn_logout.grid(row=2, column=0, padx=50, pady=10)

root.mainloop()