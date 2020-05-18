from tkinter import *
import csv
from tkinter import messagebox
from Admin_Update_Job_Offer import updateWindow
from Admin_Browse_Applications import listApp
from Admin_Add_Job_Offer import addJob
from Admin_Delete_Job_Offer import deleteJob

def verif():
    username_info = enteredName.get().strip()
    password_info = enteredPassword.get()
    try:
        ch="Administrators/"+username_info+'.CSV'
        f=open(ch,'r')
    except FileNotFoundError:
        msg = messagebox.showinfo('Error', "Create an account then Retry")
        adminSigninScreen.destroy()
    else:
        f.close()
        f = open("Administrators/Administrators.CSV", 'r')
        admins=csv.reader(f,delimiter=',')
        good=False
        for i in admins:
            try:
                x=i [0] ; y=i [1]
            except:
                continue
            else:
                if x== username_info and y == password_info:
                    good = True
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
            Button(optionsScreen, text='Add Job offer', bd=3, relief='raised', font=('system', 10), height="2",
                   width="17", command=addJob).pack(pady=12, anchor=CENTER)
            Button(optionsScreen, text='Update Job offer', bd=3, relief='raised', font=('system', 10), height="2",
                   width="17", command=updateWindow).pack(pady=12, anchor=CENTER)
            Button(optionsScreen, text='Job Seekers List', bd=3, relief='raised', font=("system", 10), height="2", width="17",
                   command=listApp).pack(pady=12, anchor=CENTER)
            Button(optionsScreen, text='Delete Job offer', bd=3, relief='raised', font=('system', 10), height="2",
                   width="17", command=deleteJob).pack(pady=12, anchor=CENTER)

            f=open('Administrators/ConnectedAdmin.txt', 'w')
            f.write(username_info)
            f.close()

            optionsScreen.mainloop()
        else:
            msg = messagebox.showinfo('Error 403', "Invalid username or password Retry")
            enteredName.delete(0,END)
            enteredPassword.delete(0,END)

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

    Label(frame, text='If this is your account valid data').grid(row=6, column=1, sticky=W)
    Button(frame, text='Log in', bd=1, relief='raised', font=("system", 5), width="6", command=verif).grid(row=6,
                                                                                                              column=2,
                                                                                                              pady=12)
    adminSigninScreen.mainloop()