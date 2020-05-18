from tkinter import *
from tkinter import messagebox
import csv

def search():
    global liste
    key_info=key.get()
    try:
        f=open('Jobs.CSV','r')
    except:
        msg=messagebox.showinfo('Error','there is no job offers')
    else:
        reader=csv.DictReader(f,delimiter=',')
        liste=list()
        if len(key_info) >= 3:
            for i in reader:
                try:
                    x = i['ID']
                    y = i['CompanyAddress']
                    z = i['RequestedDegree']
                    p = i['RequestedQualification']
                    u = i['RequestedExperience']
                    g = i['MissionDescription']
                except:
                    continue
                else:

                    if x == key_info or key_info in y or key_info in z or key_info in p or key_info in u or key_info in g:
                        liste.append(i)
                    if len(liste)==0:
                        msg1 = messagebox.showinfo('Error','no job matches your demand.Better luck next time')

                    else:
                        frame2 = LabelFrame(searchJobWindow, text='Search Results', bg='grey', font=('veranda', 30),
                                            height="100",
                                            width="2000", ).pack(anchor=CENTER)
                        Label(frame2,
                              text='Jobs which ID equal to your input OR Location/Domain Contain your input').pack()
                        r = Text(frame2, height=6, width=1000, font=('varinda', 8, 'italic'))
                        r.insert(END, liste)
                        r.pack()

        else:

              msg1=messagebox.showinfo('Error','invalid search key.Please use a search key that contains more than 2 characters ')

        f.close()



def searchWindow():
    global searchJobWindow
    global key
    searchJobWindow = Tk()
    searchJobWindow.geometry('1024x681')
    searchJobWindow.title('Search for a Job')
    searchJobWindow.pack_propagate()
    frame8=LabelFrame(searchJobWindow, text='Search for a Job', bg='grey', font=('veranda', 30), height="100",
               width="2000", ).pack(anchor=CENTER)
    Label(frame8,text='Fill in the blank the ID OR the Location OR the Domain of the Job you are searching for(length>2)').pack()
    key=Entry(frame8)
    key.pack()
    Button(frame8, text='Search', command=search).pack()

    searchJobWindow.mainloop()

