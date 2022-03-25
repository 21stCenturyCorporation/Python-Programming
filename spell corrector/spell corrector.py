from tkinter import *
from textblob import TextBlob

root = Tk()
root.geometry("400x200")
root.title("Spell Corrector in Python")
root.config(background="light green")


# Functions
def correct(*args, **kwargs):
    entry2.delete(0, END)
    input_word = str(entry1.get())

    blob = TextBlob(input_word)

    corrected_word = str(blob.correct())

    entry2.insert(10, corrected_word)


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)


label1 = Label(root, text="Welcome to Spell Corrector ", bg="red", fg="black")
label1.grid(row=0, column=0, padx=130, columnspan=10)

input_label = Label(root, text="Input Word", bg="green", fg="black")
input_label.grid(row=1, column=0, padx=20, pady=15)

correct_label = Label(root, text="Corrected Word", bg="green", fg="black")
correct_label.grid(row=3, column=0, padx=20, pady=15)

entry1 = Entry(root)
entry1.grid(row=1, column=1, padx=20)

entry2 = Entry(root)
entry2.grid(row=3, column=1, padx=20)

btn_correct = Button(root, text="Correct", bg="red", fg="black", command=correct)
btn_correct.grid(row=2, column=1, padx=20)

btn_clear = Button(root, text="Clear", bg="red", fg="black", command=clear)
btn_clear.grid(row=4, column=1, padx=20)

root.bind('<Return>', correct)

root.mainloop()
