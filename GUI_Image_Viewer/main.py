# Imported important lib files
from tkinter import *
from PIL import ImageTk,Image

# Created back button functions

def back(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(root, image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number==1:
        button_back=Button(root,text="<<",state=DISABLED)

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)


# Defined the forward button functions
def forward(image_number):
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()

    my_label=Label(root,image=image_list[image_number-1])
    my_label.grid(row=0,column=0,columnspan=3)
    button_forward=Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda: back(image_number-1))

    if image_number==4:
        button_forward=Button(root,text=">>",state=DISABLED)

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)

# Created mainscreen and added title
root = Tk()
root.title("Image Viewer application")

my_img1 = ImageTk.PhotoImage(Image.open('images/index.jpeg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/index3.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/index2.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/index3.jpeg'))


image_list = [my_img1,my_img2,my_img3,my_img4]

status = Label(root,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
status.grid(row=3,column=0,columnspan=3,sticky=W+E)
my_label=Label(root,image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

# Added buttons and pushed them to screen
button_back=Button(root,text="<<",command=back)
button_exit=Button(root,text="Exit program",command=quit,pady=10)
button_forward=Button(root,text=">>",command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

# Created mainloop
root.mainloop()