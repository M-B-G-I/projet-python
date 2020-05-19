from tkinter import *
from tkinter import messagebox
import csv
from User_Update_Application import updateWindow
from User_Add_Application import addApplication

def affich():
        id = enteredKey.get()
        fileslist = list()
        goodJobsList = list()
        f = open('Administrators/Administrators.CSV', 'r')
        reading = csv.DictReader(f, delimiter=',')
        for i in reading:
            try:
                filename = i ['AdminName']
            except:
                continue
            else:
                fileslist.append(filename+'.CSV')
        f.close()
        for i in fileslist:
            try:
                f=open('Administrators/'+i,'r')
            except:
                continue
            else:
                print('OK')
                reading=csv.DictReader(f,delimiter=',')
                for j in reading:
                    try:
                        idd=j['ID']
                        loc=j['CompanyAddress']
                        dg=j['RequestedDegree']
                        qf=j['RequestedQualification']
                        expp=j['RequestedExperience']
                        mdd=j ['MissionDescription']
                    except:
                        continue
                    else:
                        if idd==id or (id in loc) or (id in dg) or (id in qf) or (id in expp) or (id in mdd):
                            goodJobsList.append(j)
                            #goodJobsList.append('\n')

                f.close()
        if len(goodJobsList) == 0:
                    msg6 = messagebox.showerror('Error', 'No job Meets your demand and preferences, Retry later')
                    enteredKey.delete(0,END)
        else:
                    UserBrowserResult = Tk()
                    UserBrowserResult.geometry('600x700+400+0')
                    UserBrowserResult.title('Job offers Founded')
                    Label(UserBrowserResult, text='The Jobs That Meets your Demand').grid(row=0,column=0,sticky=W)
                    #goodJobsList.insert(0,my)
                    i=0
                    while i <= (len(goodJobsList)-1)*11:
                        Label(UserBrowserResult, text='Job N°'+str(i+1),fg='red').grid(row=i+1, column=0, sticky=W)
                        my=['ID','CompanyName','CompanyAddress','CompanyPhoneNumber','CompanyEmail','RequestedDegree',
                             'RequestedQualification','RequestedExperience','MissionDescription']
                        color=['#000099','#003300']
                        for j in range(9):
                             Label(UserBrowserResult, text=my[j],fg=color[j%2]).grid(row=i+j+2, column=0,sticky=W)
                             Label(UserBrowserResult, text=goodJobsList [i] [my[j]],fg=color[j%2]).grid(row=i+j+2, column=1, sticky=W)
                        i+=11
                        Button(UserBrowserResult, text='Submit New Application', bd=2, relief='raised', font=("system", 5), width="21",
                           command=addApplication).grid(row=i,column=0,sticky=W)
                        Button(UserBrowserResult, text='Update Old Application', bd=2, relief='raised', font=("system", 5),
                           width="21", command=updateWindow).grid(row=i,column=1,sticky=W)
                    UserBrowserResult.mainloop()


def ListJobOffers():
        global JobBrowser
        global enteredKey
        JobBrowser = Tk()
        JobBrowser.geometry('420x115')
        JobBrowser.title("browser")
        frame = LabelFrame(JobBrowser, text='Search for Job Offers')
        frame.grid(row=1, column=1, columnspan=10, rowspan=10)

        Label(frame, text='Enter the job ID OR Domain OR Location preferences').grid(row=2, column=1, sticky=W, pady=3)
        enteredKey = Entry(frame)
        enteredKey.grid(row=2, column=2, pady=3)

        Label(frame, text='').grid(row=6, column=1, sticky=W)
        Button(frame, text='Search', bd=1, relief='raised', font=("system", 5), width="6", command=affich).grid(row=6,
                                                                                                                column=2,
                                                                                                                pady=12)
        JobBrowser.mainloop()
ListJobOffers()