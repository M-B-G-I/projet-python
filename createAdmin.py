from tkinter import *
import csv


def Unic():
    return True

def createAdmin():
    adminScreen = Toplevel(adminScreen)
    adminScreen.geometry('512x340')
    adminScreen.title('Administrator Sign up')
    LabelFrame(adminScreen, text='Use a new username (length>0) and password (length>3)', bg='grey', font=('veranda', 10), height="50",
               width="2000", ).pack(anchor=CENTER)

    # creation

    Button(adminScreen, text='Create an Account', bd=3, relief='raised', font=("system", 10), height="2", width="30",
           command=Unic).pack(pady=12, anchor=CENTER)
    try:
        f=open("Administrators.CSV",'r+')
    except:
        f.close()
        f = open("Administrators.CSV", "w+")
        writing = csv.DictWriter(f, fieldnames=['AdminName', 'AdminPassword'], delimiter=',')
        writing.writeheader()
        writing.writerow({'AdminName': name, 'AdminPassword': password})
        f.close()
    else:
