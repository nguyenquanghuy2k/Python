
from cProfile import label
from tkinter import *

root = Tk()
# Creating a Label Widget
Mylabel1 =  Label(root, text = "Hello world").grid(row=0,column=0)
Mylabel2 =  Label(root, text = "My name's Nhan").grid(row=1, column=5)
Mylabel3 = Label(root, text= "I'm learning").grid(row=2,column= 1)

# Showing it into the screen
# Co the viet bang cach khac tach biet ra

# Mylabel1.grid(row=0, column=0)
# Mylabel2.grid(row=1, column=5)
# Mylabel3.grid(row=2,column=1)

root.mainloop() # vong lap de man hinh luon xuat hien