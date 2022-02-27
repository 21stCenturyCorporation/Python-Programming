from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("550x300")
root.resizable(False, False)

credit_1 = Label(root, text=" ")
credit_2 = Label(root, text=" ")
credit_3 = Label(root, text=" ")
credit_4 = Label(root, text=" ")

credit_1.grid(row=3, column=4)
credit_2.grid(row=4, column=4)
credit_3.grid(row=5, column=4)
credit_4.grid(row=6, column=4)

res = Label(root, text="")
res.grid(row=7, column=4)

sgpa_l = Label(root, text="")
sgpa_l.grid(row=8, column=4)
def submit():
    entry1 = str(e4.get())
    entry2 = str(e5.get())
    entry3 = str(e6.get())
    entry4 = str(e7.get())

    if entry1.isalpha() or entry2.isalpha() or entry3.isalpha() or entry4.isalpha():
        try:
            if entry1.casefold() == "A".casefold():
                credit_1["text"] = "90"
            elif entry1.casefold() == "B".casefold():
                credit_1["text"] = "80"
            elif entry1.casefold() == "C".casefold():
                credit_1["text"] = "70"
            elif entry1.casefold() == "D".casefold():
                credit_1["text"] = "50"
            elif entry1.casefold() == "E".casefold():
                credit_1["text"] = "30"
            elif entry1.casefold() == "F".casefold():
                credit_1["text"] = "0"

            if entry2.casefold() == "A".casefold():
                credit_2["text"] = "90"
            elif entry2.casefold() == "B".casefold():
                credit_2["text"] = "80"
            elif entry2.casefold() == "C".casefold():
                credit_2["text"] = "70"
            elif entry2.casefold() == "D".casefold():
                credit_2["text"] = "50"
            elif entry2.casefold() == "E".casefold():
                credit_2["text"] = "30"
            elif entry2.casefold() == "F".casefold():
                credit_2["text"] = "0"

            if entry3.casefold() == "A".casefold():
                credit_3["text"] = "90"
            elif entry3.casefold() == "B".casefold():
                credit_3["text"] = "80"
            elif entry3.casefold() == "C".casefold():
                credit_3["text"] = "70"
            elif entry3.casefold() == "D".casefold():
                credit_3["text"] = "50"
            elif entry3.casefold() == "E".casefold():
                credit_3["text"] = "30"
            elif entry3.casefold() == "F".casefold():
                credit_3["text"] = "0"

            if entry4.casefold() == "A".casefold():
                credit_4["text"] = "90"
            elif entry4.casefold() == "B".casefold():
                credit_4["text"] = "80"
            elif entry4.casefold() == "C".casefold():
                credit_4["text"] = "70"
            elif entry4.casefold() == "D".casefold():
                credit_4["text"] = "50"
            elif entry4.casefold() == "E".casefold():
                credit_4["text"] = "30"
            elif entry4.casefold() == "F".casefold():
                credit_4["text"] = "0"
            elif (len(entry1) > 1 or len(entry2) > 1 or len(entry3) > 1 or len(entry4) > 1) or (entry1 ):
                raise ValueError
            else:
                raise ValueError
            tot = int(credit_1["text"]) + int(credit_2["text"]) + int(credit_3["text"]) + int(credit_4["text"])
            sgpa = tot / 15

            res["text"] = str(tot)
            sgpa_l["text"] = str(sgpa)

        except ValueError:
            messagebox.showerror("Marksheet", "Please enter an alphabet from A - F")

# Labels
name = Label(root, text="Name")
roll = Label(root, text="Roll No.")
reg = Label(root, text="Reg No.")
sno = Label(root, text="Srl. No.")
subject = Label(root, text="Subject")
grade = Label(root, text="Grade")
sub_credit = Label(root, text="Sub Credit")
credit = Label(root, text="Credit")
total_label = Label(root, text="Total Credit")
sgpa_label = Label(root, text="SGPA")
label_1 = Label(root, text="1")
label_2 = Label(root, text="2")
label_3 = Label(root, text="3")
label_4 = Label(root, text="4")
maths = Label(root, text="Mathematics")
physics = Label(root, text="Physics")
computer = Label(root, text="Computer")
chemistry = Label(root, text="Chemistry")
str_4 = Label(root, text="4")
str_3 = Label(root, text="3")
copy_4 = Label(root, text="4")
copy_3 = Label(root, text="3")

# positioning them
name.grid(row=0, column=0)
roll.grid(row=1, column=0)
sno.grid(row=2, column=0)
label_1.grid(row=3, column=0)
label_2.grid(row=4, column=0)
label_3.grid(row=5, column=0)
label_4.grid(row=6, column=0)
subject.grid(row=2, column=1)
grade.grid(row=2, column=2)
sub_credit.grid(row=2, column=3)
credit.grid(row=2, column=4)
reg.grid(row=0, column=3)
maths.grid(row=3, column=1)
physics.grid(row=4, column=1)
computer.grid(row=5, column=1)
chemistry.grid(row=6, column=1)
str_4.grid(row=3, column=3)
copy_4.grid(row=4, column=3)
str_3.grid(row=5, column=3)
copy_3.grid(row=6, column=3)
total_label.grid(row=7, column=3)
sgpa_label.grid(row=8, column=3)

# Button
submit = Button(root, text="Submit", bg="green", fg="black", command=submit)
submit.grid(row=8, column=1)
# Entries
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)

# Positioning them
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=0, column=4)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)

root.mainloop()