from cProfile import label
from email.mime import image
from sqlite3 import Row
from tkinter import *

from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Test thoat chuong trinh")

my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/POSEIDON/Desktop/DJANGO/DJANGO/GUI_python/image/doreamon.png"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/POSEIDON/Desktop/DJANGO/DJANGO/GUI_python/image/meo.png"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/POSEIDON/Desktop/DJANGO/DJANGO/GUI_python/image/gai.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/POSEIDON/Desktop/DJANGO/DJANGO/GUI_python/image/mattroi.png"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/POSEIDON/Desktop/DJANGO/DJANGO/GUI_python/image/meo.png"))

image_list= [my_img1,my_img2,my_img3,my_img4,my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=label(image=image_list[image_number+1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))


    my_label.grid(row=0,colum=0,column_span=3)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1, column=0)


def back():
    global my_label
    global button_forward
    global button_back

button_back= Button(root, text="<<",command=back)
button_quit= Button(root, text="Thoat chuong trinh", command=root.quit) #Nut thoat chuong trinh
button_forward= Button(root,text=">>",command= lambda:forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()