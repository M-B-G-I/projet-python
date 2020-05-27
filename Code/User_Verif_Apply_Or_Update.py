from tkinter import *
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
    if new==False:
        updateWindow(JobID.get())
    else:
        addApplication(JobID.get())
    f.close()
def verifwindow():
    global JobID
    window = Tk()
    window.geometry('390x115')
    window.title("Apply or Update")
    frame = LabelFrame(window, text='Enter the ID of the job offer to Apply for or to Updated')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    Label(frame, text='Job ID from the result list').grid(row=2, column=1, sticky=W, pady=3)
    JobID = Entry(frame)
    JobID.grid(row=2, column=2, pady=3)

    Label(frame, text='Are you sure to Apply/Update this Application?').grid(row=6, column=1, sticky=W)
    B = Button(frame, text='Update', bd=1, relief='raised', font=("system", 5), width="6", command=verif).grid(
        row=6, column=2, pady=12)
    window.mainloop()
#verifwindow()