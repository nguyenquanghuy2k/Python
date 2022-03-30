# arduino_LED_user.py
#import readline
from ast import Str
from sqlite3 import connect
from struct import pack
from traceback import print_last
import serial 
import time
from tkinter import *

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM8', 9600)
root = Tk()
root.title("LCD-MITSUTOYO") #tieu de phan mem
Mylabel1 =  Label(root, text = "TOWA VIET NAM",font=("Courier", 44)).grid(row=0,column=1)
Mylabel2 =  Label(root, text = "Gia tri min",font=("Courier", 25)).grid(row=1,column=0)
Mylabel3 =  Label(root, text = "Gia tri max",font=("Courier", 25)).grid(row=2,column=0)
min1 = Entry(root,width=10, borderwidth=5,font=("Courier", 20))
min1.grid(row=1, column=2, columnspan=3)
max2 = Entry(root,width=10, borderwidth=5,font=("Courier", 20))
max2.grid(row=2, column=2, columnspan=3)

def myClick():
    cmin= (min1.get())
    cminb=bytes(cmin,'UTF-8')
    print("gia tri min:",cminb)
    time.sleep(0.1)
    ser.write(cminb)
    cmax=(max2.get())
    cmaxb=bytes(cmax,'UTF-8')
    print("gia tri max:",cmaxb)
    time.sleep(0.1)
    ser.write(cmaxb)
def ketnoi():
    ser.write(b'H') 
    kn = (ser.readline()).decode()
    kn1 = kn.rstrip()
    print(kn1)
    time.sleep(0.1)         
    if kn1 == "daketnoi":
        Mylabel4 =  Label(root, text = "CONNECTED",font=("Courier", 25)).grid(row=1,column=1)
    else :
        Mylabel5 =  Label(root, text = "CONNECTING",font=("Courier", 25)).grid(row=1,column=1)
def led_on_off():
    user_input = input("\n Type on / off / quit : ")
    if user_input =="on":
        print("LED is on...")
        time.sleep(0.1) 
        ser.write(b'H') 
        led_on_off()
    elif user_input =="off":
        print("LED is off...")
        time.sleep(0.1)
        ser.write(b'L')
        led_on_off()
    elif user_input =="quit" or user_input == "q":
        print("Program Exiting")
        time.sleep(0.1)
        ser.write(b'L')
        ser.close()
    else:
        print("Invalid input. Type on / off / quit.")
        led_on_off()
button1=Button(root,text='SEND DATA',padx= 30, pady=10,fg='#6699FF',bg='#66FF99',command=myClick) 
button2=Button(root,text='CONNECTION TEST',padx= 30, pady=10,fg='#6699FF',bg='#66FF99',command=ketnoi)
button3=Button(root,text='QUIT',padx= 30, pady=10,fg='#6699FF',bg='#66FF99',command=led_on_off)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

time.sleep(2) # wait for the serial connection to initialize 

root.mainloop() # vong lap de man hinh luon xuat hien