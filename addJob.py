from tkinter import *
from tkinter import messagebox
import csv
from tkinter import Text, Tk

def save():
    try:
        f=open("Jobs.CSV",'r')
    except:
        f = open('jobs.csv', 'w')
        if len(id.get())>=1:
            writing = csv.DictWriter(f, fieldnames=['ID', 'CompanyName', 'CompanyAddress', 'CompanyPhoneNumber',
                                                    'CompanyEmail', 'RequestedDegree', 'RequestedQualification',
                                                    'RequestedExperience', 'MissionDescription'], delimiter=',')
            writing.writeheader()
            writing.writerow({'ID': id.get(), 'CompanyName': cname.get(), 'CompanyAddress': caddress.get(),
                              'CompanyPhoneNumber': cnumber.get(), 'CompanyEmail': cemail.get(),
                              'RequestedDegree': rdg.get(), 'RequestedQualification': rqf.get("1.0",END),
                              'RequestedExperience': rexp.get("1.0",END), 'MissionDescription': t.get("1.0",END)})
            msg2 = messagebox.showinfo('Ok', "Job offer added successfully")
            JobOfferWindow.destroy()
        else:
            msg = messagebox.showinfo('Error', "Invalid ID, Retry")
            id.delete(0, END)
        f.close()

    else:
        a=csv.DictReader(f,delimiter=',')
        bad=False
        for i in a:
            if i['ID']==id.get():
                bad=True
                break
        f.close()
        if bad==False and len(id.get())>=1:
            f = open('Jobs.CSV', 'a')
            writing = csv.DictWriter(f, fieldnames=['ID', 'CompanyName', 'CompanyAddress', 'CompanyPhoneNumber',
                                                    'CompanyEmail', 'RequestedDegree', 'RequestedQualification',
                                                    'RequestedExperience', 'MissionDescription'], delimiter=',')
            writing.writerow({'ID': id.get(), 'CompanyName': cname.get(), 'CompanyAddress': caddress.get(),
                              'CompanyPhoneNumber': cnumber.get(), 'CompanyEmail': cemail.get(),
                              'RequestedDegree': rdg.get(), 'RequestedQualification': rqf.get("1.0",END),
                              'RequestedExperience': rexp.get("1.0",END), 'MissionDescription': t.get("1.0",END)})
            f.close()
            msg2 = messagebox.showinfo('Ok', "Job offer added successfully")
            JobOfferWindow.destroy()
        else:
            msg = messagebox.showinfo('Error', "Invalid ID, Retry")
            id.delete(0, END)


def addJob():
        global JobOfferWindow
        JobOfferWindow = Tk()
        JobOfferWindow.geometry('320x600')
        JobOfferWindow.title('Create a job offer')
        frame = LabelFrame(JobOfferWindow, text='Fill in the blanks the convenient job information',font=('system'))
        frame.pack()

        # creation
        global id
        global cname
        global caddress
        global cnumber
        global cemail
        global rdg
        global rqf
        global rexp
        global t

        id=StringVar()
        cname=StringVar()
        caddress=StringVar()
        cnumber=StringVar()
        cemail=StringVar()
        rdg=StringVar()
        rqf=StringVar()
        rexp=StringVar()
        t=StringVar()

        Label(frame, text='Job ID').pack()
        id = Entry(frame,font=('varinda',8,'italic'))
        id.pack()

        Label(frame, text='Company Name').pack()
        cname = Entry(frame,font=('varinda',8,'italic'))
        cname.pack()

        Label(frame, text='Company address').pack()
        caddress = Entry(frame,font=('varinda',8,'italic'))
        caddress.pack()

        Label(frame, text='Company phone Number').pack()
        cnumber = Entry(frame,font=('varinda',8,'italic'))
        cnumber.pack()

        Label(frame, text='Company Email').pack()
        cemail = Entry(frame,font=('varinda',8,'italic'))
        cemail.pack()

        Label(frame, text='Requested Degree').pack()
        rdg = Entry(frame,font=('varinda',8,'italic'))
        rdg.pack()

        Label(frame, text='Requested Qualification').pack()
        rqf = Text(frame, height=5, width=20,font=('varinda',8,'italic'))
        rqf.pack()

        Label(frame, text='Requested Experience').pack()
        rexp = Text(frame, height=5, width=20,font=('varinda',8,'italic'))
        rexp.pack()

        Label(frame, text='MissionDescription').pack()
        t = Text(frame, height=5, width=20,font=('varinda',8,'italic'))
        t.pack()


        Label(frame, text='Use this data to create your account',font=('system')).pack()
        Button(frame, text='Create', bd=1, relief='raised', font=("system", 5), width="6", command=save).pack()
        JobOfferWindow.mainloop()