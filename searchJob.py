from tkinter import *
from tkinter import messagebox
import csv

def search():
    key_info=key.get()
    try:
        f=open('jobs.csv','r')

def searchWindow():
    global searchJobWindow
    global key
    searchJobWindow = Tk()
    searchJobWindow.geometry('1024x681')
    searchJobWindow.title('Search for a Job')
    frame=LabelFrame(searchJobWindow, text='Search for a Job', bg='grey', font=('veranda', 30), height="100",
               width="2000", ).pack(anchor=CENTER)
    Label(frame,text='Fill in the blank the ID OR the Location OR the Domain of the Job you are searching for').pack()
    key=Entry(frame)
    key.pack()

    Button(frame,text='Search',command=search).pack()
#searchWindow()