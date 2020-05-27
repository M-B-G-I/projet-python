from tkinter import *
from tkinter import messagebox
import csv


def register():
    username_info = enteredName.get().strip()
    password_info = enteredPassword.get()
    try:
        ch = "Administrators/"+username_info+".CSV"
        f = open(ch, 'r')
    except FileNotFoundError:
        if len(username_info)>0 and len(password_info)>3:
            f = open("Administrators/Administrators.CSV", "a")
            writing = csv.DictWriter(f, fieldnames=['AdminName', 'AdminPassword'], delimiter=',')
            writing.writerow({'AdminName': username_info, 'AdminPassword': password_info})
            f.close()
            f = open("Administrators/"+username_info+".CSV", 'w')
            writing = csv.DictWriter(f, fieldnames=['ID', 'CompanyName', 'CompanyAddress', 'CompanyPhoneNumber',
                                                    'CompanyEmail', 'RequestedDegree', 'RequestedQualification',
                                                    'RequestedExperience', 'MissionDescription'], delimiter=',')
            writing.writeheader()
            msg = messagebox.showinfo('ok', "registration success")
            adminSignupScreen.destroy()
            f.close()
        else:
            enteredName.delete(0, END)
            enteredPassword.delete(0, END)
            msg = messagebox.showerror('Error', "Invalid username or password, Retry")
    else:
        enteredName.delete(0, END)
        enteredPassword.delete(0, END)
        msg = messagebox.showerror('Error', "Existent username, Retry")


def createAdmin():
    global adminSignupScreen
    adminSignupScreen = Tk()
    adminSignupScreen.geometry('335x125')
    adminSignupScreen.title('Administrator Sign up')
    frame = LabelFrame(adminSignupScreen, text='Use a new username (length>0) and password (length>3)')
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
    Button(frame, text='Create', bd=1, relief='raised', font=("system", 5), width="6", command=register).grid(row=6,
                                                                                                              column=2,
                                                                                                              pady=12)
    adminSignupScreen.mainloop()