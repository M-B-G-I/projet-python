from tkinter import *
from Admin_Authentication_And_Options import AdminAuthAndOp
from User_Authentication_And_Options import UserAuthAndOp
from Admin_Create_Account import createAdmin
from User_Create_Account import createUser
import csv

def BackFromaAminToMain():
    adminScreen.destroy()
    main()
def BackFromUserToMain():
    userScreen.destroy()
    main()

def AdminWindow():
    # Login Screen
    global adminScreen
    adminScreen=Tk()
    adminScreen.geometry('1024x681')
    adminScreen.title('Administrator Login')
    LabelFrame(adminScreen,text='Hello Administrator',bg='grey',font=('veranda',30),height="100", width="2000",).pack(anchor=CENTER)
    # Admin or job seeker ?
    Button(adminScreen,text='Sign in', bd=3, relief='raised', font=("system", 10), height="2", width="30",
           command=AdminAuthAndOp).pack(pady=12, anchor=CENTER)
    Button(adminScreen,text='Sign up', bd=3, relief='raised', font=('system', 10), height="2", width="30",
           command=createAdmin).pack(pady=12, anchor=CENTER)
    Button(adminScreen, text='Back to Home', bd=3, relief='raised', font=('system', 10), height="2", width="15",
           command=BackFromaAminToMain).pack(pady=12, anchor=S)
    mainScreen.destroy()
    adminScreen.mainloop()
def UserWindow():
    # Login Screen
    global userScreen
    userScreen = Tk()
    userScreen.geometry('1024x681')
    userScreen.title('User Login')
    # Sign in or Sign up
    LabelFrame(userScreen,text='Hello User',bg='grey',font=('veranda',30),height="100", width="2000",).pack(anchor=CENTER)
    Button(userScreen,text='Sign in', bd=3, relief='raised', font=("system", 10), height="2", width="30",
           command=UserAuthAndOp).pack(pady=12, anchor=CENTER)
    Button(userScreen,text='Sign up', bd=3, relief='raised', font=('system', 10), height="2", width="30", command=createUser
            ).pack(
        pady=12, anchor=CENTER)
    Button(userScreen,text='Back to Home', bd=3, relief='raised', font=('system', 10), height="2", width="15", command=BackFromUserToMain
            ).pack(
        pady=12, anchor=S)
    mainScreen.destroy()
    userScreen.mainloop()


# Main Prog
def main():
    global mainScreen
    mainScreen=Tk()
    mainScreen.geometry('1280x852')
    mainScreen.title('Recruitment')
    # import image
    bg_image = PhotoImage(file="Recruitment_bg.png")
    # set a background image
    bg_label = Label(mainScreen, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    # Admin or job seeker ?
    Button(text='Administrator',bd=3,relief='raised',font=("system", 10),height="2",width="30",command=AdminWindow).pack(pady=12,anchor=CENTER)
    Button(text='Job Seeker',bd=3,relief='raised',font=('system',10),height="2",width="30",command=UserWindow).pack(pady=12,anchor=CENTER)
    # creation od Users.CSV and Administrators.CSV
    try:
        f = open("Administrators/Administrators.CSV", "r")
    except:
        f = open("Administrators/Administrators.CSV", "w")
        writing = csv.DictWriter(f, fieldnames=['AdminName', 'AdminPassword'], delimiter=',')
        writing.writeheader()
        f.close()
    else:
        f.close()
    try:
        f = open("Users/Users.CSV", "r")
    except:
        f = open("Users/Users.CSV", "w")
        writing = csv.DictWriter(f, fieldnames=['UserName', 'UserPassword'], delimiter=',')
        writing.writeheader()
        f.close()
    else:
        f.close()
    # end creation.
    mainScreen.mainloop()

main()