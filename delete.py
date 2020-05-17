from tkinter import*
from tkinter import messagebox
def ok():
    import csv
    remove=False
    txt=EI.get()
    lines = list()
    with open('jobs.csv', 'r') as readFile:
         reader = csv.reader(readFile)
         for row in reader:
            lines.append(row)
            for field in row:
                if field ==txt :
                    lines.remove(row)
                    remove=True
                    break
         if remove==True:
            msg1 = messagebox.showinfo("delete", "job offer deleted")
         else:
            msg = messagebox.showinfo("error", "this job offer ID does not exist")
    main.destroy()
    with open('jobs.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
main = Tk()
main.title("Delete")
LI= Label(main, text="Job offer ID").grid(row=0, column=0)
EI = Entry(main, bd=5)
EI.grid(row=0, column=1)
B = Button(main, text=" Ok ", command=ok).grid(row=1, column=1)
main.mainloop()
