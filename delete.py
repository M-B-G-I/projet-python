from tkinter import*
from tkinter import messagebox
def ok():
    import csv
    txt=EI.get()
    with open('****.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['job offer ID']==txt:
                row.clear()
                msg1=messagebox.showinfo("delete","job offer deleted")
                else:
                     msg = messagebox.showinfo("error", "this job offer ID does not exist")
                    
def deleteJob():
    main = Tk()
    main.title("Delete")
    LI= Label(main, text="Job offer ID").grid(row=0, column=0)
    EI = Entry(main, bd=5)
    EI.grid(row=0, column=1)
    B = Button(main, text=" Ok ", command=ok).grid(row=1, column=1)
    main.mainloop()
