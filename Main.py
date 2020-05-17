from tkinter import *
from AdminAuthentificationAndOptionsWindow import AdminAuthAndOp
from UserAuthentificationAndOptionsWindow import UserAuthAndOp
from createAdmin import createAdmin
from createUser import createUser

def AdminWindow():
    # Login Screen
    global adminScreen
    adminScreen=Toplevel(mainScreen)
    adminScreen.geometry('1024x681')
    adminScreen.title('Administrator Login')
    LabelFrame(adminScreen,text='Hello Administrator',bg='grey',font=('veranda',30),height="100", width="2000",).pack(anchor=CENTER)
    # Admin or job seeker ?
    Button(adminScreen,text='Sign in', bd=3, relief='raised', font=("system", 10), height="2", width="30",
           command=AdminAuthAndOp).pack(pady=12, anchor=CENTER)
    Button(adminScreen,text='Sign up', bd=3, relief='raised', font=('system', 10), height="2", width="30",
           command=createAdmin).pack(pady=12, anchor=CENTER)
    adminScreen.mainloop()
def UserWindow():
    # Login Screen
    global userScreen
    userScreen = Toplevel(mainScreen)
    userScreen.geometry('1024x681')
    userScreen.title('User Login')
    # Sign in or Sign up
    LabelFrame(userScreen,text='Hello User',bg='grey',font=('veranda',30),height="100", width="2000",).pack(anchor=CENTER)
    Button(userScreen,text='Sign in', bd=3, relief='raised', font=("system", 10), height="2", width="30",
           command=UserAuthAndOp).pack(pady=12, anchor=CENTER)
    Button(userScreen,text='Sign up', bd=3, relief='raised', font=('system', 10), height="2", width="30", command=createUser
            ).pack(
        pady=12, anchor=CENTER)
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

    mainScreen.mainloop()

main()
