from tkinter import *
from tkinter import messagebox
import csv
from tkinter import Text, Tk

def save():
    f=open('Administrators/ConnectedAdmin.txt', 'r')
    admin=f.read()
    f.close()
    try:
        f=open('Administrators/'+admin+'.CSV', 'r')
    except:
        msg2 = messagebox.showinfo('Error 403', "Your are not allowed to be here! CREATE AN ACCOUNT then Retry.")
    else:
        f.close()
        adminlist=list()
        unique=True
        f=open('Administrators/Administrators.CSV','r')
        reading=csv.DictReader(f,delimiter=',')
        for i in reading:
            adminlist.append(i['AdminName']+'.CSV')
        f.close()
        for i in adminlist:
            f=open('Administrators/'+i,'r')
            reading=csv.DictReader(f,delimiter=',')
            for j in reading:
                try:
                    verif=j['ID']
                except:
                    continue
                else:
                    if verif==id.get():
                        unique=False
                        break
            f.close()
        f = open('Administrators/'+admin+'.CSV', 'a')
        if len(id.get()) >= 1 and unique==True:
            writing = csv.DictWriter(f, fieldnames=['ID', 'CompanyName', 'CompanyAddress', 'CompanyPhoneNumber',
                                                    'CompanyEmail', 'RequestedDegree', 'RequestedQualification',
                                                    'RequestedExperience', 'MissionDescription'], delimiter=',')
            writing.writerow({'ID': id.get(), 'CompanyName': cname.get(), 'CompanyAddress': caddress.get(),
                              'CompanyPhoneNumber': cnumber.get(), 'CompanyEmail': cemail.get(),
                              'RequestedDegree': rdg.get(), 'RequestedQualification': rqf.get("1.0", END),
                              'RequestedExperience': rexp.get("1.0", END), 'MissionDescription': t.get("1.0", END)})
            msg2 = messagebox.showinfo('Ok', "Job offer added successfully")
            JobOfferWindow.destroy()
        elif unique==False and len(id.get()) >= 1:
            msg3 = messagebox.showerror('Error', "This Job Offer ID is already used! Try to use an unique Job ID")
        else:
            msg4 = messagebox.showerror('Error', "Use an ID which length >=1")
        f.close()

def addJob():
        global JobOfferWindow
        JobOfferWindow = Tk()
        JobOfferWindow.geometry('320x600+400+0')
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
