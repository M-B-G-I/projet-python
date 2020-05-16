from tkinter import *

def AdminWindow():
    screen1=Toplevel(mainScreen)
    screen1.geometry('1024x681')
    screen1.title('Administrator Login')
    

def UserWindow():
    screen1 = Toplevel(mainScreen)
    screen1.geometry('1024x681')
    screen1.title('User Login')

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
    # Sing in in Sign up page
    mainScreen.mainloop()
main()