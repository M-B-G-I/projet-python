def createAdmin():
    import tkinter as tk

    def onClick_create():
        import csv
        AdminName = e1.get()
        AdminPassword = e2.get()
        try:
            f = open('Administrators.CSV', 'r')
        except FileNotFoundError:
            if len(AdminName) > 0 and len(AdminPassword) > 3:
                f = open("Administrators.CSV", "w")
                writing = csv.DictWriter(f, fieldnames=['AdminName', 'AdminPassword'], delimiter=',')
                writing.writeheader()
                writing.writerow({'AdminName': AdminName, 'AdminPassword': AdminPassword})
                f.close()
            else:
                tk.Label(window, fg="red", text='Invalid Username or Password, Please Retry').grid(row=3)
        else:
            adimns = csv.reader(f, delimiter=',')
            bad=False
            for i in adimns:
                if AdminName == i[0] or AdminPassword == i[1] or len(AdminName) <= 0 or len(AdminPassword) <= 3:
                    tk.Label(window, fg="red", text='Invalid Username or Password, Please Retry').grid(row=3)
                    bad=True
                    break
            if bad==False:
                f.close()
                f = open("Administrators.CSV", "a")
                writing = csv.DictWriter(f, fieldnames=['AdminName', 'AdminPassword'], delimiter=',')
                writing.writerow({'AdminName': AdminName, 'AdminPassword': AdminPassword})
                f.close()

    def onClick_exit():
        window.destroy()
        exit()

    window = tk.Tk()
    window.title("Create a new Administrator")
    tk.Label(window, text="User Name").grid(row=0, column=0)
    tk.Label(window, text="Password").grid(row=1, column=0)

    e1 = tk.Entry(window, width=35)
    e2 = tk.Entry(window, width=35)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(text='Create', width=6, command=onClick_create()).grid(row=2, column=0, pady=12, padx=12, sticky=tk.W)
    tk.Button(text='Exit', width=4, command=onClick_exit()).grid(row=2, column=1, pady=12, sticky=tk.W)

    window.mainloop()


createAdmin()
