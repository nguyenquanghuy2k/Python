from tkinter import *

from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Test thoat chuong trinh")

my_img = ImageTk.PhotoImage(Image.open("C:/Users/POSEIDON/Desktop/DJANGO/DJANGO/GUI_python/image/doreamon.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit= Button(root, text="Thoat chuong trinh", command=root.quit) #Nut thoat chuong trinh
button_quit.pack()

root.mainloop()