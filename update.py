from tkinter import *
from tkinter import messagebox
import csv
def apply():
    import csv
    with open('addApp.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writing = csv.DictWriter(file, fieldnames=['ID','Name','address','phone number','university degree','experience','skills'], delimiter=',')
        writing.writeheader()
        writer.writerow([E8.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get()])
        msg = messagebox.showinfo("add application","your application has been added")
def update():
    global E2
    global E3
    global E4
    global E5
    global E6
    global E7
    id=E8.get()
    import csv
    with open('addApp.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['ID']==id:
                main = Tk()
                main.title("update")
                L2= Label(main, text="name").grid(row=1, column=0)
                E2 = Entry(main, bd=5)
                E2.grid(row=1, column=1)
                row['name']=E2.get()
                L3= Label(main, text="address").grid(row=2, column=0)
                E3 = Entry(main, bd=5)
                E3.grid(row=2, column=1)
                row['address']=E3.get()
                L4= Label(main, text="phone number").grid(row=3, column=0)
                E4 = Entry(main, bd=5)
                E4.grid(row=3, column=1)
                row['phone number']=E4.get()
                L5= Label(main, text="university degree").grid(row=4, column=0)
                E5 = Entry(main, bd=5)
                E5.grid(row=4, column=1)
                row['university degree']=E5.get()
                L6= Label(main, text="professional experience").grid(row=5, column=0)
                E6 = Entry(main, bd=5)
                E6.grid(row=5, column=1)
                row['professional experience']=E6.get()
                L7= Label(main, text="skills").grid(row=6, column=0)
                E7 = Entry(main, bd=5)
                E7.grid(row=6,column=1)
                row['skills']=E7.get()
                B4= Button(main, text=" update ", command=apply).grid(row=7, column=1)
                main.mainloop()
def updateApp():
    main = Tk()
    main.title("update")
    L8 = Label(main, text="ID").grid(row=0, column=0)
    E8 = Entry(main, bd=5)
    E8.grid(row=0, column=1)
    B3 = Button(main, text=" Update ", command=update).grid(row=1, column=1)
    main.mainloop()

