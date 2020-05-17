from tkinter import *
import csv
from tkinter import messagebox
from updateJob import updateJob
from listApp import list
from addJob import addJob
from delete import deleteJob

def verif():
    username_info = enteredName.get()
    password_info = enteredPassword.get()
    try:
        f = open("Administrators.CSV", 'r')
    except FileNotFoundError:
        msg = messagebox.showinfo('Error', "Create an account then Retry")
        adminSigninScreen.destroy()
    else:
        admins=csv.reader(f,delimiter=',')
        good=False
        for i in list(admins)[0:-1:2]:
            if i[0]==username_info and i[1]==password_info:
                good=True
                break
        f.close()
        if good==True:
            adminSigninScreen.destroy()
            # list of options
            optionsScreen=Tk()
            optionsScreen.geometry("1024x681")
            optionsScreen.title("Administrators Options")
            LabelFrame(optionsScreen, text='Services', bg='grey', font=('veranda', 30), height="100",
                       width="2000", ).pack(anchor=CENTER)
            Button(optionsScreen, text='Job Seekers List', bd=3, relief='raised', font=("system", 10), height="2", width="11",
                   command=list).pack(pady=12, anchor=CENTER)
            Button(optionsScreen, text='Add Job offer', bd=3, relief='raised', font=('system', 10), height="2", width="13",
                   command=addJob).pack(pady=12, anchor=CENTER)
            Button(optionsScreen, text='Update Job offer', bd=3, relief='raised', font=('system', 10), height="2",
                   width="16", command=updateJob).pack(pady=12, anchor=CENTER)
            Button(optionsScreen, text='Delete Job offer', bd=3, relief='raised', font=('system', 10), height="2",
                   width="17", command=deleteJob).pack(pady=12, anchor=CENTER)
            optionsScreen.mainloop()

            # creation
            global enteredName
            global enteredPassword

            Label(frame, text=' Username').grid(row=2, column=1, sticky=W, pady=3)
            enteredName = Entry(frame)
            enteredName.grid(row=2, column=2, pady=3)

            Label(frame, text=' Password').grid(row=5, column=1, sticky=W)
            enteredPassword = Entry(frame, show='*')
            enteredPassword.grid(row=5, column=2)

            Label(frame, text='Use this data to create your account').grid(row=6, column=1, sticky=W)
            Button(frame, text='Log in', bd=1, relief='raised', font=("system", 5), width="6", command=verif).grid(
                row=6, column=2, pady=12)
            adminSigninScreen.mainloop()
        else:
            enteredName.delete(0, END)
            enteredPassword.delete(0, END)
            msg = messagebox.showinfo('Error 403', "Wrong username or password, Retry")


def AdminAuthAndOp():
    global adminSigninScreen
    adminSigninScreen = Tk()
    adminSigninScreen.geometry('335x125')
    adminSigninScreen.title('Administrator Sign in')
    frame = LabelFrame(adminSigninScreen, text='Enter your Username and your Password')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    # creation
    global enteredName
    global enteredPassword

    Label(frame, text=' Username').grid(row=2, column=1, sticky=W, pady=3)
    enteredName = Entry(frame)
    enteredName.grid(row=2, column=2, pady=3)

    Label(frame, text=' Password').grid(row=5, column=1, sticky=W)
    enteredPassword = Entry(frame, show='*')
    enteredPassword.grid(row=5, column=2)

    Label(frame, text='Use this data to create your account').grid(row=6, column=1, sticky=W)
    Button(frame, text='Log in', bd=1, relief='raised', font=("system", 5), width="6", command=verif).grid(row=6,
                                                                                                              column=2,
                                                                                                              pady=12)
    adminSigninScreen.mainloop()