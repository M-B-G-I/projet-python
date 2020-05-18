from tkinter import *
import csv
from tkinter import messagebox
#from searchJob import searchWindow
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

def ListAppliedJobs():
    AppliedJobsListWindow = Tk()
    AppliedJobsListWindow.geometry('335x125')
    AppliedJobsListWindow.title('The Jobs you are applied for')
    frame = LabelFrame(AppliedJobsListWindow, text='The list of Jobs IDs which you are applied for')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)
    AppliedJobsListWindow.mainloop()

def verif():
    username_info = enteredName.get()
    password_info = enteredPassword.get()
    try:
        f = open("Administrators.CSV", 'r')
    except FileNotFoundError:
        msg = messagebox.showinfo('Error', "Create an account then Retry")
        userSigninScreen.destroy()
    else:
        users=csv.reader(f,delimiter=',')
        good=False
        for i in users:
            try:
                x=i [0] ; y=i [1]
            except:
                continue
            else:
                if x== username_info and y == password_info:
                    good = True
                    break
        f.close()
        if good==True:
            userSigninScreen.destroy()
            # list of options
            userOptionsScreen=Tk()
            userOptionsScreen.geometry("1024x681")
            userOptionsScreen.title("User Options")
            LabelFrame(userOptionsScreen, text='Services', bg='grey', font=('veranda', 30), height="100",
                       width="2000", ).pack(anchor=CENTER)
            Button(userOptionsScreen, text='Search Job Offer', bd=3, relief='raised', font=("system", 10), height="2", width="24",
                   command=searchWindow).pack(pady=12, anchor=CENTER)
            Button(userOptionsScreen, text='The Jobs you applied for', bd=3, relief='raised', font=('system', 10), height="2",
                   width="24", command=ListAppliedJobs).pack(pady=12, anchor=CENTER)
            userOptionsScreen.mainloop()
        else:
            msg = messagebox.showinfo('Error 403', "Invalid username or password Retry")
            enteredName.delete(0,END)
            enteredPassword.delete(0,END)

def UserAuthAndOp():
    global userSigninScreen
    userSigninScreen = Tk()
    userSigninScreen.geometry('335x125')
    userSigninScreen.title('User Sign in')
    frame = LabelFrame(userSigninScreen, text='Enter your Username and your Password')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    # creation
    global enteredName
    global enteredPassword

    Label(frame, text=' Username').grid(row=2, column=1, sticky=W, pady=3)
    enteredName = Entry(frame)
    enteredName.grid(row=2, column=2, pady=3)

    Label(frame, text=' Password').grid(row=5, column=1, sticky=W)
    enteredPassword = Entry(frame, show='*')
    enteredPassword.grid(row=5, column=2)

    Label(frame, text='If this is your account valid data').grid(row=6, column=1, sticky=W)
    Button(frame, text='Log in', bd=1, relief='raised', font=("system", 5), width="6", command=verif).grid(row=6,
                                                                                                              column=2,
                                                                                                              pady=12)
    userSigninScreen.mainloop()
#UserAuthAndOp()