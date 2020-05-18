from tkinter import *
from tkinter import messagebox
import csv

def searchWindow():
    global searchJobWindow
    searchJobWindow = Tk()
    searchJobWindow.geometry('1024x681')
    searchJobWindow.title('Search for a Job')
    LabelFrame(searchJobWindow, text='Search for a Job', bg='grey', font=('veranda', 30), height="100",
               width="2000", ).pack(anchor=CENTER)
    Button(searchJobWindow, text='', bd=3, relief='raised', font=("system", 10), height="2", width="30",
           #command=AdminAuthAndOp
           ).pack(pady=12, anchor=CENTER)
    Button(searchJobWindow, text='', bd=3, relief='raised', font=('system', 10), height="2", width="30",
           #command=createAdmin
           ).pack(pady=12, anchor=CENTER)
    searchJobWindow.mainloop()
#searchWindow()