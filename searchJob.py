from tkinter import *
from tkinter import messagebox
import csv
def searchJob():
    info = enteredinfo.get()
    f = open("Jobs.CSV",'r')
    reader = csv.DictReader(f)
    exist = False
    l = []
    for row in reader:
        if row['ID'] == info:
            exist = True
            l.append(row)
        elif row['Domain'] == info:
            exist = True
            l.append(row)
        elif row['Location'] == info:
            exist = True
            l.append(row)
    main = Tk()
    main.title("Jobs available")
    k = 1
    for i in l:
        Label(main,text=i).grid(row=k,column=0)
        k = k + 1
    main.mainloop()
    if exist == False:
        info.delete(0, END)
        msg = messagebox.showinfo('Error', "No Job available. Maybe next time.")

def searchWindow():
    global enteredinfo
    searchScreen = Tk()
    searchScreen.geometry('1024x681')
    searchScreen.title('Search Job')
    #ID/Domain/location
    LabelFrame(searchScreen, text='Search Job', bg='grey', font=('veranda', 30), height="100", width="2000", ).pack(
        anchor=CENTER)
    Label(Frame, text='Enter the ID, location or the Domain of the Job:').grid(row=2, column=1, sticky=W, pady=3)
    enteredinfo = Entry(Frame)
    enteredinfo.grid(row=2, column=2, pady=3)
    #Button
    Button(Frame, text='search', bd=1, relief='raised', font=("system", 5), width="6",
           command=searchJob).grid(row=6, column=2, pady=12)
    searchScreen.mainloop()
