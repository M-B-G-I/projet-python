from tkinter import *
import csv
from tkinter import messagebox
from tkinter import ttk

def affich():
    global goodAppsList
    id=enteredID.get()
    IDlist = list()
    fileslist = list()
    goodAppsList = list()
    if 'ALL' in id.upper():
        f=open('Administrators/'+admin+'.CSV','r')
        reading=csv.DictReader(f,delimiter=',')
        for i in reading:
            try:
                ids=i['ID']
            except:
                continue
            else:
                IDlist.append(ids)
        f.close()
        f=open('Users/Users.CSV', 'r')
        reading = csv.DictReader(f, delimiter=',')
        for i in reading:
            try:
                name = i ['UserName']
            except:
                continue
            else:
                fileslist.append(name+'.CSV')
        f.close()
        for i in fileslist:
            f = open('Users/'+i, 'r')
            reading=csv.DictReader(f,delimiter=",")
            for j in reading:
                try:
                    xyz=j['JobID']
                except:
                    continue
                else:
                    if xyz in IDlist:
                        goodAppsList.append(j)
            f.close()
        adminBrowserResult = Tk()
        adminBrowserResult.geometry('600x700+400+0')
        adminBrowserResult.title('Application(s) Founded')
        Label(adminBrowserResult, text='The Application(s) That Meets your Demand ('+str(len(goodAppsList))+' Application(s))').grid(
            row=0, column=0, sticky=W)
        # goodJobsList.insert(0,my)
        i = 0
        while i < len(goodAppsList)*9:
            Label(adminBrowserResult, text='Application N°'+str(i%8+1), fg='red').grid(row=i+1, column=0, sticky=W)
            my = ['Name','Address','PhoneNumber','Email','UniversityDegree','Experience','Skills','JobID']
            color = ['#000099', '#003300']
            for j in range(8):
                Label(adminBrowserResult, text=my [j], fg=color [j%2]).grid(row=i+j+2, column=0, sticky=W)
                Label(adminBrowserResult, text=goodAppsList [i%8] [my [j]], fg=color [j%2]).grid(row=i+j+2, column=1,
                                                                                                 sticky=W)
            i += 9
        adminBrowserResult.mainloop()
# Not ALL
    else:
        exist=False
        f = open("Administrators/"+admin+".CSV", 'r')
        reading=csv.DictReader(f,delimiter=',')
        for i in reading:
            try:
                x=i['ID']
            except:
                continue
            else:
                if x==id:
                    exist=True
                    break
        f.close()
# Existent ID
        if exist==True:
            f=open('Users/Users.CSV', 'r')
            reading=csv.DictReader(f,delimiter=',')
            for i in reading:
                try:
                    xx=i['UserName']
                except:
                    continue
                else:
                    fileslist.append(xx+'.CSV')
            f.close()
            for i in fileslist:
                try:
                    f=open('Users/'+i.strip(),'r')
                except:
                    continue
                else:
                    reading=csv.DictReader(f,delimiter=',')
                    for j in reading:
                        try:
                            yy=j['JobID']
                        except:
                            continue
                        else:
                            if yy==id:
                                goodAppsList.append(j)
                            else:
                                continue
                    f.close()
            # No one applied
            if len(goodAppsList)==0:
                msg5=messagebox.showerror('Error','No one applied for your job offer yet, Retry later')
            # not(No one applied)
            else:
                adminBrowserResult = Tk()
                adminBrowserResult.geometry('600x700+400+0')
                adminBrowserResult.title('Application(s) Founded')
                Label(adminBrowserResult, text='The Application(s) That Meets your Demand ('+str(
                    len(goodAppsList))+' Application(s))').grid(row=0, column=0, sticky=W)
                # goodJobsList.insert(0,my)
                i = 0
                while i < len(goodAppsList)*9:
                    Label(adminBrowserResult, text='Application N°'+str(i%8+1), fg='red').grid(row=i+1, column=0, sticky=W)
                    my = ['Name', 'Address', 'PhoneNumber', 'Email', 'UniversityDegree', 'Experience', 'Skills',
                          'JobID']
                    color = ['#000099', '#003300']
                    for j in range(8):
                        Label(adminBrowserResult, text=my [j], fg=color [j%2]).grid(row=i+j+2, column=0, sticky=W)
                        Label(adminBrowserResult, text=goodAppsList [i%8] [my [j]], fg=color [j%2]).grid(row=i+j+2,
                                                                                                         column=1,
                                                                                                         sticky=W)
                    i += 9
                adminBrowserResult.mainloop()
#Non existent ID
        else:
            msg3=messagebox.showerror("Error","You did not added a job offer with this ID, Create One then Retry!")
def listApp():
    global admin
    f = open('Administrators/ConnectedAdmin.txt', 'r')
    admin = f.read()
    f.close()
    global AppBrowser
    global enteredID
    AppBrowser = Tk()
    AppBrowser.geometry('350x115')
    AppBrowser.title("browser")
    frame = LabelFrame(AppBrowser, text='Search for the applications of an offer you created as an Admin')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    Label(frame, text='Enter the job offer ID OR "ALL"').grid(row=2, column=1, sticky=W, pady=3)
    enteredID = Entry(frame)
    enteredID.grid(row=2, column=2, pady=3)

    Label(frame, text='').grid(row=6, column=1, sticky=W)
    Button(frame, text='Search', bd=1, relief='raised', font=("system", 5), width="6", command=affich).grid(row=6,
                                                                                                           column=2,
                                                                                                           pady=12)
    AppBrowser.mainloop()
