def createAdmin():
    import tkinter as tk
    import tkinter.messagebox

    def onClick_create(name,passw):
        import csv
        AdminName = name.get()
        AdminPassword = passw.get()
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
                tk.Label(window, fg="red", text='Invalid Username or Password, Please Retry').grid(row=6)
        else:
            admins = csv.reader(f, delimiter=',')
            bad=False
            for i in admins:
                if AdminName == i[0] or AdminPassword == i[1] or len(AdminName) <= 0 or len(AdminPassword) <= 3:
                    tk.Label(window, fg="red", text='Invalid Username or Password, Please Retry').grid(row=6)
                    bad=True
                    break
            if bad==False:
                f.close()
                f = open("Administrators.CSV", "a")
                writing = csv.DictWriter(f, fieldnames=['AdminName', 'AdminPassword'], delimiter=',')
                writing.writerow({'AdminName': AdminName, 'AdminPassword': AdminPassword})
                f.close()

    window = tk.Tk()
    window.title("Create a new Administrator")
    frame = tk.LabelFrame(window, text='Login')
    frame.grid(row=1, column=1, columnspan=10, rowspan=10)

    tk.Label(frame, text=' Usename ').grid(row=2, column=1, sticky=tk.W)
    username = tk.Entry(frame)
    username.grid(row=2, column=2)

    tk.Label(frame, text=' Password ').grid(row=5, column=1, sticky=tk.W)
    password = tk.Entry(frame, show='*')
    password.grid(row=5, column=2)

    tk.Button(text='Create', width=6, command=onClick_create(username,password)).grid(row=2, column=0, pady=12, padx=12, sticky=tk.W)

    window.mainloop()


createAdmin()
