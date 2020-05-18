from tkinter import *
from tkinter import messagebox
import csv

def save():
        f=open("Jobs.CSV", 'r')
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
                    a[indice]={'ID': info['ID'], 'CompanyName': cname.get(), 'CompanyAddress': caddress.get(),
                              'CompanyPhoneNumber': cnumber.get(), 'CompanyEmail': cemail.get(),
                              'RequestedDegree': rdg.get(), 'RequestedQualification': rqf.get("1.0",END),
                              'RequestedExperience': rexp.get("1.0",END), 'MissionDescription': t.get("1.0",END)}
            indice+=1
        f.close()
        f = open('Jobs.CSV', 'w')
        writing = csv.DictWriter(f, fieldnames=['ID', 'CompanyName', 'CompanyAddress', 'CompanyPhoneNumber',
                                                'CompanyEmail', 'RequestedDegree', 'RequestedQualification',
                                                'RequestedExperience', 'MissionDescription'], delimiter=',')
        writing.writeheader()
        for i in a:
            writing.writerow(i)
        f.close()
        msg2 = messagebox.showinfo('Ok', "Job offer added successfully")
        JobOfferWindow.destroy()


def update():
        global JobOfferWindow
        JobOfferWindow = Tk()
        JobOfferWindow.geometry('600x700+400+0')
        JobOfferWindow.title('Update job offer')
        frame = LabelFrame(JobOfferWindow, text='Update the convenient information about the job which ID='+info['ID'],font=('system'))
        frame.pack()

        # creation
        global cname
        global caddress
        global cnumber
        global cemail
        global rdg
        global rqf
        global rexp
        global t

        cname=StringVar()
        caddress=StringVar()
        cnumber=StringVar()
        cemail=StringVar()
        rdg=StringVar()
        rqf=StringVar()
        rexp=StringVar()
        t=StringVar()


        Label(frame, text='Company Name').pack()
        cname = Entry(frame,font=('varinda',8,'italic'))
        cname.insert(END, info ['CompanyName'])
        cname.pack()

        Label(frame, text='Company address').pack()
        caddress = Entry(frame,font=('varinda',8,'italic'))
        caddress.insert(END,info['CompanyAddress'])
        caddress.pack()

        Label(frame, text='Company phone Number').pack()
        cnumber = Entry(frame,font=('varinda',8,'italic'))
        cnumber.insert(END,info['CompanyPhoneNumber'])
        cnumber.pack()

        Label(frame, text='Company Email').pack()
        cemail = Entry(frame,font=('varinda',8,'italic'))
        cemail.insert(END,info['CompanyEmail'])
        cemail.pack()

        Label(frame, text='Requested Degree').pack()
        rdg = Entry(frame,font=('varinda',8,'italic'))
        rdg.insert(END,info ['RequestedDegree'])
        rdg.pack()

        Label(frame, text='Requested Qualification').pack()
        rqf = Text(frame, height=6, width=22,font=('varinda',8,'italic'))
        rqf.insert(END, info ['RequestedQualification'])
        rqf.pack()

        Label(frame, text='Requested Experience').pack()
        rexp = Text(frame, height=6, width=22,font=('varinda',8,'italic'))
        rexp.insert(END,info['RequestedExperience'])
        rexp.pack()

        Label(frame, text='MissionDescription').pack()
        t = Text(frame, height=6, width=22,font=('varinda',8,'italic'))
        t.insert(END, info['MissionDescription'])
        t.pack()


        Label(frame, text='Use this data to create your account',font=('system')).pack()
        Button(frame, text='Update', bd=1, relief='raised', font=("system", 5), width="6", command=save).pack()
        JobOfferWindow.mainloop()

def updateJob():
    Code = EI.get()
    try:
        f = open("Jobs.CSV", 'r')
    except:
        msg1 = messagebox.showinfo("Error", "Create job offer then Retry")
    else:
        reader = csv.DictReader(f,delimiter=",")
        exist = False
        for row in reader:
            try:
                x=row['ID']
            except:
                continue
            else:
                if Code == x:
                    exist = True
                    # Copier coller aala mtaa l add job
                    global info
                    info=row
                    update()
                if exist == False:
                    EI.delete(0, END)
                    msg = messagebox.showinfo('Error', "non-existent Job ID, Retry!")
        f.close()



def updateWindow():
    global main
    global EI
    main = Tk()
    main.geometry('335x115')
    main.title("Delete")
    frame = LabelFrame(main, text='Enter the ID of the job offer to be Updated')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    Label(frame, text=' ID').grid(row=2, column=1, sticky=W, pady=3)
    EI = Entry(frame)
    EI.grid(row=2, column=2, pady=3)

    Label(frame, text='Are you sure to Update this job offer?').grid(row=6, column=1, sticky=W)
    B = Button(frame, text='Update', bd=1, relief='raised', font=("system", 5), width="6", command=updateJob).grid(row=6,
                                                                                                            column=2,
                                                                                                            pady=12)
    main.mainloop()

#updateWindow()
