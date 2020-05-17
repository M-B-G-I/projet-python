from tkinter import *
from tkinter import messagebox
import csv


def register():
    username_info = enteredName.get()
    password_info = enteredPassword.get()
    try:
        f = open("Users.CSV", 'r')
    except FileNotFoundError:
        if len(username_info) > 0 and len(password_info) > 3:
            f = open("Users.CSV", "w")
            writing = csv.DictWriter(f, fieldnames=['UserName', 'Password'], delimiter=',')
            writing.writeheader()
            writing.writerow({'UserName': username_info, 'Password': password_info})
            f.close()
            enteredName.delete(0, END)
            enteredPassword.delete(0, END)
            msg = messagebox.showinfo('success', "registration success!")
            userSignupScreen.destroy()
        else:
            enteredName.delete(0, END)
            enteredPassword.delete(0, END)
            msg = messagebox.showinfo('Error', "Invalid username or password, Retry")
    else:
        users = csv.reader(f, delimiter=',')
        bad = False
        for i in users:
            try:
                x = i[0]
            except:
                continue
            else:
                if x == username_info:
                    bad = True
                    break
        f.close()
        if bad == False and len(username_info) > 0 and len(password_info) > 3:
            f = open("Users.CSV", 'a')
            writing = csv.DictWriter(f, fieldnames=['UserName', 'Password'], delimiter=',')
            writing.writerow({'UserName': username_info, 'Password': password_info})
            f.close()
            enteredName.delete(0, END)
            enteredPassword.delete(0, END)
            msg = messagebox.showinfo('success', "registration success!")
            userSignupScreen.destroy()
        else:
            enteredName.delete(0, END)
            enteredPassword.delete(0, END)
            msg = messagebox.showinfo('Error', "Invalid username or password, Retry")

def createUser():
    global userSignupScreen
    userSignupScreen = Tk()
    userSignupScreen.geometry('335x125')
    userSignupScreen.title('User Sign up')
    frame = LabelFrame(userSignupScreen, text='Use a new username (length>0) and password (length>3)')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    # creation
    global name
    global password
    global enteredName
    global enteredPassword

    name=StringVar()
    password=StringVar()

    Label(frame, text=' Username').grid(row=2, column=1, sticky=W,pady=3)
    enteredName = Entry(frame)
    enteredName.grid(row=2, column=2,pady=3)

    Label(frame, text=' Password').grid(row=5, column=1, sticky=W)
    enteredPassword = Entry(frame, show='*')
    enteredPassword.grid(row=5, column=2)

    Label(frame,text='Use this data to create your account').grid(row=6,column=1,sticky=W)
    Button(frame, text='Create', bd=1, relief='raised', font=("system", 5),width="6",
           command=register).grid(row=6,column=2,pady=12)