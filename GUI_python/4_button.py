
from tkinter import *

root = Tk()

def myClick():
    mylabel = Label(root, text="Look ! I click a Button!!!")
    mylabel.pack()

Mybutton = Button(root,text="Click me!!!", padx=50, pady=50) #padx la chieu rong la truc x, pady la chieu cao truc y, state = DISABLED la khoa khong cho nhan button
Mybutton.pack()
Mybutton = Button(root,text="Click me!!!", command=myClick,fg="blue",bg="red") # fg la font chu, bg la background cua nut
Mybutton.pack()

root.mainloop() # vong lap de man hinh luon xuat hien