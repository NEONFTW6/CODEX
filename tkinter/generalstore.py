from tkinter import *
from tkinter import messagebox as mbox


DEEPTHA = Tk()
DEEPTHA.title("generalstore.exe")
DEEPTHA.geometry("1000x1000")
img = PhotoImage(file="D:\intro and outro\channels4_profile.png")  
DEEPTHA.iconphoto(False,img)


head = Label(text="GENERAL STORE",relief=SUNKEN,font="comicsansms 16 bold",borderwidth=6,bg="black",fg="white")
head.pack(fill=X)

f1= Frame(DEEPTHA)
f1.pack(side=LEFT,anchor="nw",padx=10,pady=10)

flabel= Label(f1,text="NAME :",relief=SUNKEN,font="comicsansms 13 bold")
flabel.grid(row=0,column=1,padx=10,pady=10)

slabel= Label(f1,text="PRODUCT :",relief=SUNKEN,font="comicsansms 13 bold")
slabel.grid(row=1,column=1,padx=10,pady=10)

tlabel= Label(f1,text="QUANTITY :",relief=SUNKEN,font="comicsansms 13 bold")
tlabel.grid(row=2,column=1,padx=10,pady=10)

f4label= Label(f1,text="PAYMENT :",relief=SUNKEN,font="comicsansms 13 bold")
f4label.grid(row=3,column=1,padx=10,pady=10)

name = StringVar()
product = StringVar()
quantity = IntVar()
payment = StringVar()
check = IntVar()

nameentry = Entry(f1, textvariable=name)
productentry = Entry(f1, textvariable=product)
quantityentry = Entry(f1, textvariable=quantity)
paymententry = Entry(f1, textvariable=payment)


nameentry.grid(row=0,column=2)
productentry.grid(row=1,column=2)
quantityentry.grid(row=2,column=2)
paymententry.grid(row=3,column=2) 


def reset():
     with open("record.txt") 


def checkbox():
    if check.get() == 1:
        button.config(state=NORMAL)
    else:
        button.config(state=DISABLED)


def submit():
        
        print(f"REGISTERED:{name.get(),product.get(),quantity.get(),payment.get()}")

        with open("record.txt","a") as f:
             f.write(f"REGISTERED:{name.get(),product.get(),quantity.get(),payment.get()}\n")

             name.set("")
             product.set("")         
             quantity.set(0)
             payment .set("")
             check.set(0)
             button.config(state=DISABLED)

         
checkboxes=Checkbutton(f1,text="Agree terms and condition!",font="comicsansms 8 bold",bg="white",variable=check,command=checkbox)
checkboxes.grid(row=4,column=2)

button=Button(f1,text="REGISTER",state=DISABLED,font="comicsansms 10 bold",command=submit)
button.grid(row=6,column=2,pady=5)

button=Button(f1,text="Delete",font="lucida 10 bold",command=reset)
button.grid()




DEEPTHA.mainloop()

    