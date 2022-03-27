from tkinter import *
import time

root = Tk()
root.title("Digital Clock")
root.config(background="violet")
root.resizable(False, False)

def timer():
	times = time.strftime("%H:%M:%S %p")
	label['text'] = times
	label.after(1000, timer)

label = Label(root, text="", font=("DS-Digital", 30, "bold"), foreground="white", background="violet", padx=5, pady=5)
label.pack()

timer()

root.mainloop()