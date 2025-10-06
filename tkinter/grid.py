from tkinter import *

root=Tk()
root.title("Dance Form")
root.geometry("500x250")
root.maxsize(500,250)


head =Label(root,text="DANCE FORM",relief=SUNKEN,bg="grey",font="comicsansms 16 bold",fg="black",borderwidth=3)
head.pack(fill=X)

f1= Frame(root,bg="grey",relief=SUNKEN,borderwidth=4 )
f1.pack(fill=X)


flabel= Label(f1,text="Username", bg="black",fg="white",borderwidth=3,relief=SUNKEN,font="   bold")
flabel.grid(padx=23,pady=23)

Slabel= Label(f1,text="Art style",relief=SUNKEN, bg="black",fg="white",borderwidth=3,font="    bold")
Slabel.grid(row=1,pady=23,padx=23)



user =StringVar()
art = StringVar()


userentry= Entry(f1, textvariable=user)
artentry = Entry(f1,textvariable=art)

userentry.grid(row=0,column=1)
artentry.grid(row=1,column=1)

def getvals():
    print(f"The username is {user.get()}")
    print(f"The artstyle is {art.get()}")

Button(f1,text="SUBMIT",command=getvals).grid(pady=23)


root.mainloop()