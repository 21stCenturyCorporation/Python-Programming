from tkinter import *  # For creating widgets
from random import *   # for choosing values
from PIL import ImageTk, Image  # For solving problem with tkinter

root = Tk()
root.geometry("409x400")

win_list = ['Rock', 'Paper', 'Scissor']


def reset():
    stone.config(state="active")
    paper.config(state="active")
    scissor.config(state="active")
    text_area.delete("0.0", END)

def disable_buttons():
    stone.config(state="disable")
    paper.config(state="disable")
    scissor.config(state="disable")


def isrock():
    comp = choice(win_list)
    if ("Rock" == comp):
        text_area.insert("0.0", "The match is a draw\n")
        disable_buttons()
    elif (comp == "Paper"):
        text_area.insert("0.0", "Computer has won the match\n")
        disable_buttons()
    elif (comp == "Scissor"):
        text_area.insert("0.0", "You have won the match\n")
        disable_buttons()

def isscissor():
    comp = choice(win_list)
    if ("Scissor" == comp):
        text_area.insert("0.0", "The match is a draw\n")
        disable_buttons()
    elif (comp == "Paper"):
        text_area.insert("0.0", "You have won the match\n")
        disable_buttons()
    elif (comp == "Rock"):
        text_area.insert("0.0", "Computer has won the match\n")
        disable_buttons()

def ispaper():
    comp = choice(win_list)
    if ("Paper" == comp):
        text_area.insert("0.0", "The match is a draw\n")
        disable_buttons()
    elif (comp == "Rock"):
        text_area.insert("0.0", "You have won the match\n")
        disable_buttons()
    elif (comp == "Scissor"):
        text_area.insert("0.0", "Computer has won the match\n")
        disable_buttons()

img = ImageTk.PhotoImage(Image.open("game.jpg"))  # PIL solution

label = Label(root, image=img)
label.place(x=0, y=0)

paper = Button(root, text="Paper", font=("Montserrat", 13, "bold"), command=isrock)
paper.place(x=150, y=10)

stone = Button(root, text="Rock", font=("Montserrat", 13, "bold"), command=isrock)
stone.place(x=150, y=60)

scissor = Button(root, text="Scissor", font=("Montserrat", 13, "bold"), command=isrock)
scissor.place(x=150, y=110)

text_area = Text(root, width=53, height=10, font=("Montserrat", 10,"bold"))
text_area.place(x=0, y=160)

reset_btn = Button(root, text="Reset Game",width=26,font=("Montserrat", 13, "bold"),foreground="red",bg="black", command=reset)
reset_btn.place(x = 50, y = 350)
root.mainloop()