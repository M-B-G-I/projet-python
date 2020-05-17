from tkinter import*
from tkinter import messagebox
def ok():
    import csv
    txt=EI.get()
    with open('Jobs.CSV', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['ID']==txt:
                row.clear()
                msg1=messagebox.showinfo("delete","job offer deleted")
            else:
                msg = messagebox.showinfo("error", "this job offer ID does not exist")
                    
def deleteJob():
    global EI
    main = Tk()
    main.title("Delete")
    Label(main, text="Job offer ID").grid(row=0, column=0)
    EI = Entry(main, bd=5)
    EI.grid(row=0, column=1)
    Button(main, text=" delete ", command=ok).grid(row=1, column=1,width=6)
    main.mainloop()
