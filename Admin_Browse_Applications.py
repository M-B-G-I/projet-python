from tkinter import *
import csv
from tkinter import messagebox
from tkinter import ttk

def affich():
    global AdminBrowserResult
    id=enteredID.get()
    AdminBrowserResult = Tk()
    AdminBrowserResult.geometry('600x700+400+0')
    AdminBrowserResult.title('Update job offer')

    AdminBrowserResult.mainloop()

def listApp():
    global admin
    f = open('Administrators/ConnectedAdmin.txt', 'r')
    admin = f.read()
    f.close()
    global AppBrowser
    global enteredID
    AppBrowser = Tk()
    AppBrowser.geometry('335x115')
    AppBrowser.title("browser")
    frame = LabelFrame(AppBrowser, text='Enter the ID of the job offer which you need to see the Applications')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    Label(frame, text=' ID').grid(row=2, column=1, sticky=W, pady=3)
    enteredID = Entry(frame)
    enteredID.grid(row=2, column=2, pady=3)

    Label(frame, text='Are you sure to delete this job offer?').grid(row=6, column=1, sticky=W)
    Button(frame, text='delete', bd=1, relief='raised', font=("system", 5), width="6", command=affich).grid(row=6,
                                                                                                           column=2,
                                                                                                           pady=12)
    AppBrowser.mainloop()

''''def listing():
    listee=list()
    IDinfo=SearchedID.get()
    IDinfo=IDinfo.strip().upper()
    if 'ALL' in IDinfo:
        f=open('Users/Users.CSV','r')
        aaa=csv.DictReader(f,delimiter=',')
        aa=list(aaa)
        f.close()
        for i in aa:
            g=open('aa','r')
            listee.append(i)
            g.close()

    else:
        f = open('Users/Users.CSV', 'r')
        aaa = csv.DictReader(f, delimiter=',')
        aa = list(aaa)
        f.close()
        for i in aa:
            g = open('aa', 'r')
            if i['JobID']==IDinfo:
                listee.append(i)
            g.close()
    Label(listWindow, text='Requested Experience').pack()
    tt = Text(listWindow, height=5, width=20, font=('varinda', 8, 'italic'))
    tt.insert(END,listee)
    tt.pack()
def list():
    # 'Administrators/'+admin+'.CSV'
    global SearchedID
    global admin
    f = open('Administrators/ConnectedAdmin.txt', 'r')
    admin = f.read()
    global listWindow
    listWindow = Tk()
    listWindow.geometry('800x532')
    listWindow.title('Brows the list of job seekers')

    try:
        f=open("Administrators/"+admin+".CSV", 'r')
    except:
        msg2 = messagebox.showinfo('Error 403', "Your are not allowed to be here! CREATE AN ACCOUNT then Retry.")
    else:
        global jobs
        jobs=csv.DictReader(f,delimiter=',')
        Label(listWindow,text='Enter the ID of the Job which applications you need to list').pack(pady=12,anchor=CENTER)
        SearchedID=Entry(listWindow)
        SearchedID.pack()
        Button(listWindow,text='Browse',command=listing).pack(pady=12,anchor=CENTER)
        f.close()
    listWindow.mainloop()'''
