from cgitb import text
from tkinter import *

root = Tk()

e = Entry(root,width=50, bg="blue", fg="white",borderwidth=5)
e.pack()
e.insert(0,"Enter your name: ") # xuat hien mac dinh dong chu

def myClick():
    mylabel = Label(root, text="Hello " + e.get())
    mylabel.pack()

#dung cach kahc de dinh nghia ham cho de dang hon
#def myClick():
#    hello= "Hello " + e.get()
#    mylabel = Label(root, text=hello)
#   mylabel.pack()


Mybutton = Button(root,text="Click me!!!", command=myClick,fg="blue",bg="red")
Mybutton.pack()

root.mainloop() # vong lap de man hinh luon xuat hien