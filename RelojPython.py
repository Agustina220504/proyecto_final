from tkinter import *
from time import strftime

ven=Tk()
ven.title("Reloj")
ven.resizable(width=0, height=0)

clockFormat='%H:%M:%S %p'
textFont="calibri"

def time():
    string=strftime(clockFormat)
    label.config(text =string)
    label.after(1000, time)

label=Label(ven,font=('calibri', 100),background="light blue",foreground="black")
label.pack(anchor="center")

time()
ven.mainloop()
