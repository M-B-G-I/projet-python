from tkinter import *
import csv
from tkinter import messagebox
from User_Browse_Job_Offers import ListJobOffers


def verif():
    username_info = enteredName.get().strip()
    password_info = enteredPassword.get()
    try:
        ch="Users/"+username_info+'.CSV'
        f=open(ch,'r')
    except FileNotFoundError:
        msg = messagebox.showinfo('Error', "Create an account then Retry")
        UserSigninScreen.destroy()
    else:
        f.close()
        f = open("Users/Users.CSV", 'r')
        users=csv.reader(f,delimiter=',')
        good=False
        for i in users:
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
            UserSigninScreen.destroy()
            # list of options
            optionsScreen=Tk()
            optionsScreen.geometry("1024x681")
            optionsScreen.title("Users Options")
            LabelFrame(optionsScreen, text='Services', bg='grey', font=('veranda', 30), height="100",
                       width="2000", ).pack(anchor=CENTER)
            Button(optionsScreen, text='Search for job offers', bd=3, relief='raised', font=('system', 10), height="2",
                   width="17", command=ListJobOffers).pack(pady=12, anchor=CENTER)

            f=open('Users/ConnectedUsers.txt', 'w')
            f.write(username_info)
            f.close()

            optionsScreen.mainloop()
        else:
            msg = messagebox.showinfo('Error 403', "Invalid username or password Retry")
            enteredName.delete(0,END)
            enteredPassword.delete(0,END)

def UserAuthAndOp():
    global UserSigninScreen
    UserSigninScreen = Tk()
    UserSigninScreen.geometry('335x125')
    UserSigninScreen.title('Users Sign in')
    frame = LabelFrame(UserSigninScreen, text='Enter your Username and your Password')
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
    UserSigninScreen.mainloop()
#UserAuthAndOp()