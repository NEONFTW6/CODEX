from tkinter import *

Baseroot = Tk()
Baseroot.geometry("500x500")
Baseroot.title("Frames")

f1= Frame(Baseroot,bg="grey",borderwidth="6")
f1.pack(side=LEFT,fill=Y)

f2= Frame(Baseroot,bg="grey",borderwidth="6")
f2.pack(side=TOP,fill=X)


blabel = Label(f1,text="Welcome Guys",fg="white",bg="black",borderwidth="5",font="Helvetica 15 bold", relief=SUNKEN)
blabel.pack(pady=120)

blabel = Label(f2,text="Welcome to Tkinter",fg="white",bg="black",borderwidth="5",font="comicsansms 15 bold", relief=SUNKEN)
blabel.pack(padx=120)


Baseroot.mainloop()