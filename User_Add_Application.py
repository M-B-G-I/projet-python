from tkinter import*
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
import csv
from tkinter import Text, Tk

def save2():
    f=open('Users/ConnectedUsers.txt','r')
    User=f.read()
    f.close()
    try:
        f=open('Users/'+User+'.CSV', 'r')
    except:
        msg2 = messagebox.showinfo('Error 403', "Your are not allowed to be here! CREATE AN ACCOUNT then Retry.")
    else:
        f.close()
        f = open('Users/'+User+'.CSV', 'a')
        if len(UserID.get()) >= 1:
            writing = csv.DictWriter(f, fieldnames=['ID','Name','Address','PhoneNumber','Email','UniversityDegree',
                                                    'Experience','Skills','JobID'], delimiter=',')
            writing.writerow({'ID': UserID.get(), 'Name': UserName.get(), 'Address': UserAdress.get(),
                              'PhoneNumber': UserNumber.get(), 'Email': UserEmail.get(),
                              'UniversityDegree': UserUniversityDegree.get(), 'Experience': UserExp.get("1.0", END),
                              'Skills': UserSkills.get("1.0", END), 'JobID': JobID.get()})
            msg2 = messagebox.showinfo('Ok', "Job offer added successfully")
            JobOfferWindow.destroy()
        f.close()

def addApplication():
        global JobOfferWindow
        JobOfferWindow = Tk()
        JobOfferWindow.geometry('320x600+400+0')
        JobOfferWindow.title('apply for a job')
        frame = LabelFrame(JobOfferWindow, text='Fill in the blanks with your informations',font=('system'))
        frame.pack()

        # creation
        global UserID
        global UserName
        global UserAdress
        global UserNumber
        global UserEmail
        global UserUniversityDegree
        global UserExp
        global UserSkills
        global JobID

        UserID=StringVar()
        UserName=StringVar()
        UserAdress=StringVar()
        UserNumber=StringVar()
        UserEmail=StringVar()
        UserUniversityDegree=StringVar()
        UserExp=StringVar()
        UserSkills=StringVar()
        JobID=StringVar()

        Label(frame, text='ID of the job you want to apply for').pack()
        JobID = Entry(frame, font=('varinda', 8, 'italic'))
        JobID.pack()

        Label(frame, text='''Your ID card (Be Careful)''').pack()
        UserID = Entry(frame, font=('varinda', 8, 'italic'))
        UserID.pack()

        Label(frame, text='Your Name').pack()
        UserName = Entry(frame, font=('varinda', 8, 'italic'))
        UserName.pack()

        Label(frame, text='Your address').pack()
        UserAdress = Entry(frame, font=('varinda', 8, 'italic'))
        UserAdress.pack()

        Label(frame, text='your phone Number').pack()
        UserNumber = Entry(frame, font=('varinda', 8, 'italic'))
        UserNumber.pack()

        Label(frame, text='your Email').pack()
        UserEmail = Entry(frame, font=('varinda', 8, 'italic'))
        UserEmail.pack()

        Label(frame, text='Your Degree').pack()
        UserUniversityDegree = Entry(frame, font=('varinda', 8, 'italic'))
        UserUniversityDegree.pack()

        Label(frame, text='Your Qualification').pack()
        UserExp = Text(frame, height=5, width=20, font=('varinda', 8, 'italic'))
        UserExp.pack()

        Label(frame, text='Your Experience').pack()
        UserSkills = Text(frame, height=5, width=20, font=('varinda', 8, 'italic'))
        UserSkills.pack()


        Label(frame, text='Use this data to Apply ',font=('system')).pack()
        Button(frame, text='Apply', bd=1, relief='raised', font=("system", 5), width="6", command=save2).pack()
        JobOfferWindow.mainloop()
#addApplication()