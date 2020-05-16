from tkinter import *

def main():
    mainScreen=Tk()
    mainScreen.geometry('1280x852')
    mainScreen.title('Recruitment')
    # import image
    bg_image = PhotoImage(file="Recruitment_bg.png")
    # set a background image
    bg_label = Label(mainScreen, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    # Admin or job seeker ?
    Button(text='Administrator',bd=3,relief='raised',font=("system", 10)).pack(pady=12)
    Button(text='Job Seeker',bd=3,relief='raised',font=('system',10)).pack(pady=12)
    # Sing in in Sign up page
    mainScreen.mainloop()
main()