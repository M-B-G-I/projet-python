from tkinter import *
from tkinter import messagebox
import csv
def listing():

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
    listWindow.mainloop()


