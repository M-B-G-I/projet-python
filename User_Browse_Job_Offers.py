from tkinter import *
from tkinter import messagebox
import csv
def listing():

    '''listee=list()
    IDinfo=enteredID.get()
    IDinfo=IDinfo.strip().upper()
    if 'ALL' in IDinfo:
        f=open('Administrators/Administrators.CSV','r')
        aaa=csv.DictReader(f,delimiter=',')
        aa=list(aaa)
        f.close()
        for i in aa:
            g=open('aa','r')
            listee.append(i)
            g.close()
    else:
        f = open('Administrators/Administrators.CSV', 'r')
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
    tt.pack()'''
def list():
    # 'Administrators/'+admin+'.CSV'
    global enteredID
    global user
    liste=list()
    f=open('Administrators/Administrators.CSV','r')
    b=csv.reader(f,delimiter=',')
    for i in b:
        g=open('Administrators/'+i[0]+'.CSV','r')
        a=csv.DictReader(g,delimiter=',')
        for j in a:
            liste.append(j)
        g.close()
    f.close()
    f=open('jobs.txt','w')
    f.write(liste)
    f.close()
    global listWindow
    listWindow = Tk()
    listWindow.geometry('800x532')
    listWindow.title('Brows the list of jobs')

    Label(listWindow,text='Enter the ID of the Job which applications you need to list').pack(pady=12,anchor=CENTER)
    enteredID=Entry(listWindow).pack(pady=12,anchor=CENTER)
    Button(listWindow,text='Browse',command=listing).pack(pady=12,anchor=CENTER)
    listWindow.mainloop()'''


