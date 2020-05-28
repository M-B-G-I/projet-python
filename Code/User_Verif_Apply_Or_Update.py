from tkinter import *
from tkinter import messagebox
import csv
from Code.User_Update_Application import updateWindow
from Code.User_Add_Application import addApplication

def verif():
    global User
    f=open('Users/ConnectedUsers.txt', 'r')
    User=f.read()
    f.close()
    f=open('Users/'+User+'.CSV','r')
    reading=csv.DictReader(f,delimiter=',')
    new=True
    for i in reading:
        try:
            yy=i['JobID']
        except:
            continue
        else:
            #print(yy,'**',JobID.get(),'**',yy==JobID.get(),'**',yy=='1515')
            if yy==JobID.get():
                new=False
                break
    f.close()
    fileslist=list()
    f=open('Administrators/Administrators.CSV','r')
    reading=csv.DictReader(f,delimiter=',')
    for i in reading:
        try:
            name=i['AdminName']
        except:
            continue
        else:
            fileslist.append(name+'.CSV')
    f.close()
    exist=False
    for i in fileslist:
        f=open('Administrators/'+i,'r')
        reading=csv.DictReader(f,delimiter=',')
        for j in reading:
            try:
                idd=j['ID']
            except:
                continue
            else:
                if idd==JobID.get():
                    exist=True
                    break
        f.close()
    if exist==False:
        msg6=messagebox.showerror('Error','Unfounded Job ID')
        window.destroy()
    else:
        if new == False:
            updateWindow(JobID.get(),window)
        else:
            addApplication(JobID.get(),window)

def verifwindow():
    global JobID
    global window
    window = Tk()
    window.geometry('390x115')
    window.title("Apply or Update")
    frame = LabelFrame(window, text='Enter the ID of the job offer to Apply for or to Updated')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    Label(frame, text='Job ID from the result list').grid(row=2, column=1, sticky=W, pady=3)
    JobID = Entry(frame)
    JobID.grid(row=2, column=2, pady=3)

    Label(frame, text='Are you sure to Apply/Update this Application?').grid(row=6, column=1, sticky=W)
    B = Button(frame, text='Apply/Update', bd=1, relief='raised', font=("system", 5), width="12", command=verif).grid(
        row=6, column=2, pady=12)
    window.mainloop()
#verifwindow()