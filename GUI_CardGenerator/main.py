from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("MANIT card generater")
head = ImageTk.PhotoImage(Image.open("index.jpeg"))

top = Label(root, image=head)
top.grid(row=0, column=0, columnspan=2)
gender = None

f_name_text = Label(root, text="Enter your first name: ")
f_name_text.grid(row=1, column=0)

first_name = Entry(root)
first_name.insert(1, "Shanu")
first_name.grid(row=1, column=1)

l_name_text = Label(root, text="Enter your last name: ")
l_name_text.grid(row=2, column=0)

last_name = Entry(root)
last_name.insert(1, "Sharma")
last_name.grid(row=2, column=1)

branch_text = Label(root, text="Enter your branch:   ")
branch_text.grid(row=3, column=0)

branch = Entry(root)
branch.grid(row=3, column=1)

scholer_text = Label(root, text="Enter your Scholernumber:")
scholer_text.grid(row=4, column=0)

scholer = Entry(root)
scholer.grid(row=4, column=1)

dob_text = Label(root, text="Enter your DOB number:")
dob_text.grid(row=5, column=0)

dob = Entry(root)
dob.grid(row=5, column=1)

gender_text = Label(root, text="Select your gender: :")
gender_text.grid(row=6, column=0)

var = IntVar()
Radiobutton(root, text="Male", variable=var, value=1).grid(row=6, column=1)
Radiobutton(root, text="Female", variable=var, value=2).grid(row=7, column=1)
Radiobutton(root, text="Others", variable=var, value=3).grid(row=8, column=1)


def onclick():
    new_window = Toplevel(root)
    header = ImageTk.PhotoImage(Image.open("index.jpeg"))

    top = Label(new_window, image=head)
    top.grid(row=0, column=0, columnspan=2)
    n="Name: " + first_name.get() + last_name.get()
    name = Label(new_window,text=n)
    name.grid(row=1,column=0,columnspan=2)
    b = "Branch: "+branch.get()
    branchnew = Label(new_window,text=b)
    branchnew.grid(row=2,column=0,columnspan=2)
    sch = "Scholer no: "+ str(scholer.get())
    scholer1 = Label(new_window,text=sch)
    scholer1.grid(row=3,column=0,columnspan=2)
    d = "Date or birth: "+str(dob.get())
    dob1 = Label(new_window,text=d)
    dob1.grid(row=4,column=0,columnspan=2)
    if var==1:
        gender = "Male"
    elif var==2:
        gender = "Female"
    elif var==3:
        gender = "Others"
    g = "Gender: " + gender
    gen = Label(new_window,text = g)
    gen.grid(row=5,column=0,columnspan=2)

button = Button(root, text="Submit", command=onclick)
button.grid(row=9, column=0, columnspan=2)

mainloop()
