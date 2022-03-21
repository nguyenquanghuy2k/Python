
import math
from tkinter import *

root = Tk()
root.title("Simple Calculator") #tieu de phan mem

e = Entry(root,width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx= 30, pady= 30)

def button_click(number):
    #e.delete(0, END)
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

#define Buttons
button1= Button(root, text='THEM', padx=30, pady= 20)
button2= Button(root, text='XOA', padx=30, pady= 20)
button3= Button(root,text='SUA', padx=30,pady=20)

# Put the button on the screen

button1.grid(row= 1, column=0)
button2.grid(row = 2, column = 1)
button3.grid(row = 3, column = 2)



root.mainloop() # vong lap de man hinh luon xuat hien