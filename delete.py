from tkinter import*
from tkinter import messagebox

def ok():
    import csv
    remove=False
    txt=EI.get()
    lines = list()
    try:
        f=open('jobs.csv', 'r')
    except:
        msg1 = messagebox.showinfo("Error", "Create job offer then Retry")
    else:
        reader = csv.DictReader(f,delimiter=',')
        remove=False
        for row in reader:
            if row['ID']!=txt:
                lines.append(row)
            elif row ['ID']==txt:
                remove=True
        if remove == True:
            msg1 = messagebox.showinfo("delete", "job offer deleted")
        else:
            msg = messagebox.showinfo("error", "this job offer ID does not exist")
            f.close()
    main.destroy()

    f=open('jobs.csv', 'w')
    writing = csv.DictWriter(f, fieldnames=['ID', 'CompanyName', 'CompanyAddress', 'CompanyPhoneNumber', 'CompanyEmail', 'RequestedDegree',
                     'RequestedQualification', 'RequestedExperience', 'MissionDescription'], delimiter=',')
    writing.writeheader()
    for i in lines:
        writing.writerow(i)
    f.close()
def deleteJob():
    global main
    global EI
    main = Tk()
    main.geometry('335x115')
    main.title("Delete")
    frame = LabelFrame(main, text='Enter the ID of the job offer to be deleted')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    Label(frame, text=' ID').grid(row=2, column=1, sticky=W, pady=3)
    EI = Entry(frame)
    EI.grid(row=2, column=2, pady=3)

    Label(frame, text='Are you sure to delete this job offer?').grid(row=6, column=1, sticky=W)
    B=Button(frame, text='delete', bd=1, relief='raised', font=("system", 5), width="6", command=ok).grid(row=6,
                                                                                                           column=2,
                                                                                                           pady=12)
    main.mainloop()