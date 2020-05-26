from tkinter import *
import csv
from tkinter import messagebox
from tkinter import ttk

def affich():
    id=enteredID.get()
    IDlist = list()
    fileslist = list()
    goodUsersList = list()
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
        f=open('../Users/Users.CSV', 'r')
        reading = csv.DictReader(f, delimiter=',')
        for i in reading:
            try:
                name = i ['UserName']
            except:
                continue
            else:
                fileslist.append(name+'.CSV')
        f.close()
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
        if exist==True:
            f=open('../Users/Users.CSV', 'r')
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
                                goodUsersList.append(j)
                                goodUsersList.append('\n')
                            else:
                                continue
                    f.close()
            if len(goodUsersList)==0:
                msg5=messagebox.showerror('Error','No one applied for your job offer yet, Retry later')
            else:
                AdminBrowserResult = Tk()
                AdminBrowserResult.geometry('600x700+400+0')
                AdminBrowserResult.title('Update job offer')
                Label(AdminBrowserResult, text='the people who applied for this job are').pack()
                tx = Text(AdminBrowserResult, height=600, width=500, font=('varinda',11, 'italic'))
                tx.insert(END, goodUsersList)
                tx.pack()
                AdminBrowserResult.mainloop()

        else:
            msg3=messagebox.showerror("Error","You did not added a job offer with this ID, Create One then Retry!")
def listApp():
    global admin
    f = open('../Administrators/ConnectedAdmin.txt', 'r')
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
#listApp()