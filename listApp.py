from tkinter import *
import csv
from tkinter import messagebox

from addapplication import apply


def list():
    global listWindow
    listWindow = Tk()
    listWindow.geometry('800x532')
    listWindow.title('Brows the list of job seekers')
    '''Button(text='Administrator', bd=3, relief='raised', font=("system", 10), height="2", width="30",
           command=AdminWindow).pack(pady=12, anchor=CENTER)
    Button(text='Job Seeker', bd=3, relief='raised', font=('system', 10), height="2", width="30",
           command=UserWindow).pack(pady=12, anchor=CENTER)'''
    try:
        f=open("Jobs.CSV",'r')
    except FileNotFoundError:
        msg = messagebox.showinfo('Error', "Create an offer then Retry")
        listWindow.destroy()
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
        v = StringVar()
        v.set(listeOptions [0])
        om = om = OptionMenu(listWindow, v, *listeOptions)
        om.pack()
        f.close()
    Button(text='Browse',bd=3,relief='raised',font=("system", 10),height="2",width="30",command=print(v.get())).pack(pady=12,anchor=CENTER)
    listWindow.mainloop()
list()