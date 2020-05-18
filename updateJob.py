from tkinter import *
from tkinter import messagebox
import csv

def updateJob():
    Code = enteredCode.get()
    f = open("Jobs.CSV", 'r')
    reader = csv.DictReader(f)
    f.close()
    exist = False
    for row in reader:
        if Code == reader['ID']:
            exist = True
            # Copier coller aala mtaa l add job
    if exist == False :
        enteredCode.delete(0, END)
        msg = messagebox.showinfo('Error', "non-existent Job ID, Retry!")



def updateWindow():
    global enteredCode
    updateScreen = Tk()
    updateScreen.geometry('1024x681')
    updateScreen.title('Update Job')
    #Code
    LabelFrame(updateScreen, text='Update Job', bg='grey', font=('veranda', 30), height="100", width="2000", ).pack(
        anchor=CENTER)
    Label(frame, text='Job Offer Code:').grid(row=2, column=1, sticky=W, pady=3)
    enteredCode = Entry(frame)
    enteredCode.grid(row=2, column=2, pady=3)
    #Button
    Button(Frame, text='Update', bd=1, relief='raised', font=("system", 5), width="6",
           command=updateJob).grid(row=6, column=2, pady=12)
    updateScreen.mainloop()

updateWindow()
