from tkinter import *
import csv
from tkinter import messagebox

def listing():
    listee=list()
    IDinfo=enteredID.get()
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
    global enteredID
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
        jobs=csv.DictReader(f,delimiter=',')
        listeOptions = ['All']
        for i in jobs:
            try:
                x=i['ID']
            except:
                continue
            else:
                listeOptions.append(i ['ID'])
        f.close()
        Label(listWindow,text='Enter the ID of the Job which applications you need to list').pack(pady=12,anchor=CENTER)
        enteredID=Entry(listWindow).pack(pady=12,anchor=CENTER)
        Button(listWindow,text='Browse',command=listing).pack(pady=12,anchor=CENTER)
    listWindow.mainloop()
#list()