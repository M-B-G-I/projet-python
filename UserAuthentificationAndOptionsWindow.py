from tkinter import *
import csv
from tkinter import messagebox

def verif():
    username_info = enteredName.get()
    password_info = enteredPassword.get()
    try:
        f = open("Users.CSV", 'r')
    except FileNotFoundError:
        msg = messagebox.showinfo('Error', "non-existent account")
        userSigninScreen.destroy()
    else:
        users=csv.reader(f,delimiter=',')
        good=False
        for i in list(users)[0:-1:2]:
            if i[0]==username_info and i[1]==password_info:
                good=True
                break
        f.close()
        if good==True:
            msg = messagebox.showinfo('ok', "log in success!")
            userSigninScreen.destroy()
            # list of options
        else:
            enteredName.delete(0, END)
            enteredPassword.delete(0, END)
            msg = messagebox.showinfo('Error', "Wrong username or password, Retry")


def UserAuthAndOp():
    global userSigninScreen
    userSigninScreen = Tk()
    userSigninScreen.geometry('335x125')
    userSigninScreen.title('User Sign in')
    frame = LabelFrame(userSigninScreen, text='Enter your Username and your Password')
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
    userSigninScreen.mainloop()