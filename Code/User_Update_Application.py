from tkinter import *
from tkinter import messagebox
import csv

def save():
        f=open('Users/'+user+'.CSV', 'r')
        a=csv.DictReader(f,delimiter=',')
        a=list(a)
        indice=0
        for i in a:
            try:
                id=i['ID']
            except:
                continue
            else:
                if id==info['ID']:
                    a[indice]={'ID': UserCode, 'Name': UserName.get(), 'Address': UserAddress.get(),
                              'PhoneNumber': UserNumber.get(), 'Email': UserEmail.get(),
                              'UniversityDegree': Userdegree.get(), 'Experience': UserExperience.get("1.0", END),
                              'Skills': UserSkills.get("1.0", END),'JobID':Code}
            indice+=1
        f.close()
        f = open('Users/'+user+'.CSV', 'w')
        writing = csv.DictWriter(f, fieldnames=['ID','Name','Address','PhoneNumber','Email','UniversityDegree','Experience','Skills','JobID'], delimiter=',')
        writing.writeheader()
        for i in a:
            writing.writerow(i)
        f.close()
        msg2 = messagebox.showinfo('Ok', "Job application Update successfully")
        JobApplicationWindow.destroy()


def update():
        #print(list(info))
        global JobApplicationWindow
        JobApplicationWindow = Tk()
        JobApplicationWindow.geometry('600x700+400+0')
        JobApplicationWindow.title('the user with ID='+UserCode+' will Update his application for job with ID='+Code)
        frame = LabelFrame(JobApplicationWindow, text='Update the convenient information about the job which ID=' + info['ID'], font=('system'))
        frame.pack()

        # creation
        global UserName
        global UserAddress
        global UserNumber
        global UserEmail
        global Userdegree
        global UserExperience
        global UserSkills


        UserName=StringVar()
        UserAddress=StringVar()
        UserNumber=StringVar()
        UserEmail=StringVar()
        Userdegree=StringVar()
        UserExperience=StringVar()
        UserSkills=StringVar()


        Label(frame, text='Your Name').pack()
        UserName = Entry(frame, font=('varinda', 8, 'italic'))
        UserName.insert(END, info ['Name'])
        UserName.pack()

        Label(frame, text='Your Address').pack()
        UserAddress = Entry(frame, font=('varinda', 8, 'italic'))
        UserAddress.insert(END, info['Address'])
        UserAddress.pack()

        Label(frame, text='Your Phone Number').pack()
        UserNumber = Entry(frame, font=('varinda', 8, 'italic'))
        UserNumber.insert(END, info['PhoneNumber'])
        UserNumber.pack()

        Label(frame, text='Your Email').pack()
        UserEmail = Entry(frame, font=('varinda', 8, 'italic'))
        UserEmail.insert(END, info['Email'])
        UserEmail.pack()

        Label(frame, text='Your Degree').pack()
        Userdegree = Entry(frame, font=('varinda', 8, 'italic'))
        Userdegree.insert(END, info ['UniversityDegree'])
        Userdegree.pack()

        Label(frame, text='Your Experience').pack()
        UserExperience = Text(frame, height=6, width=22, font=('varinda', 8, 'italic'))
        UserExperience.insert(END, info ['Experience'])
        UserExperience.pack()

        Label(frame, text='Your Skills').pack()
        UserSkills = Text(frame, height=6, width=22, font=('varinda', 8, 'italic'))
        UserSkills.insert(END, info['Skills'])
        UserSkills.pack()

        Label(frame, text='Use this data to update your job',font=('system')).pack()
        Button(frame, text='Update ', bd=1, relief='raised', font=("system", 5), width="6", command=save).pack()
        JobApplicationWindow.mainloop()

def updateJob():
    global info
    global user
    global Code
    global UserCode
    UserCode=UserID.get()
    Code = AppIdToBeUpdated
    f = open('Users/ConnectedUsers.txt', 'r')
    user= f.read()
    f.close()
    #print(user)
    try:
        f = open('Users/'+user+'.CSV', 'r')
    except:
        msg2 = messagebox.showinfo('Error 403', "Your are not allowed to be here! CREATE AN ACCOUNT then Retry.")
    else:
        reader = csv.DictReader(f,delimiter=",")
        exist = False
        for row in reader:
            try:
                x=row['ID']
                y=row['JobID']
            except:
                continue
            else:
                #print(x,"*",y)
                if Code == y and UserCode==x:
                    exist = True
                    info=row
                    update()
                else:
                    msg2 = messagebox.showinfo('Error 403',"Your ID is incorrect.Please try again!")

        f.close()



def updateWindow(xyz):
    global main
    global AppIdToBeUpdated
    global UserID
    main = Tk()
    main.geometry('335x115')
    main.title("Update")
    frame = LabelFrame(main, text='Enter the ID of the job offer to be Updated')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    Label(frame, text='Your ID').grid(row=2, column=1, sticky=W, pady=3)
    UserID = Entry(frame)
    UserID.grid(row=2, column=2, pady=3)

    AppIdToBeUpdated=xyz
    '''Label(frame, text='Job ID (From the Search Result)').grid(row=3, column=1, sticky=W, pady=3)
    AppIdToBeUpdated = Entry(frame)
    AppIdToBeUpdated.grid(row=3, column=2, pady=3)'''

    Label(frame, text='Are you sure to Update this Application?').grid(row=6, column=1, sticky=W)
    B = Button(frame, text='Update', bd=1, relief='raised', font=("system", 5), width="6", command=updateJob).grid(row=6,
                                                                                                            column=2,
                                                                                                            pady=12)
    main.mainloop()

#updateWindow()
