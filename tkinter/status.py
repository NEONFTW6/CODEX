from tkinter import *


def upload():
    statusvar.set("Editing")
    nbar.update()
    import time
    time.sleep(2)
    statusvar.set("Edited by Neel")

root = Tk()
root.geometry("500x500") 
root.title("Status bar")


statusvar = StringVar()
statusvar.set("Edit By Neel")
nbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
nbar.pack(side=BOTTOM,fill=X)

Button(text="Status",command=upload,width=13,cursor="hand2").pack()


root.mainloop()