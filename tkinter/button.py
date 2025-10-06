from tkinter import *

root = Tk()
root.geometry("500x500")

def tk():
    print("Welcome to Tkinter!")

def td():
    print("Today we learned buttons")

def hap():
    print("I am so happy")

def tq():
    print("Thank you so much")


frame = Frame(root, borderwidth=7, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1 = Button(frame, bg="green", text="Tkinter is op",font="comicsansms 16 bold", command=tk)
b1.pack(side=LEFT)

b2 = Button(frame, bg="green", text="Tkinter is op",font="comicsansms 16 bold", command=td)
b2.pack(side=LEFT)

b3 = Button(frame, bg="green", text="Tkinter is op",font="comicsansms 16 bold", command=hap)
b3.pack(side=LEFT)

b4 = Button(frame, bg="green", text="Tkinter is op",font="comicsansms 16 bold", command=tq)
b4.pack(side=LEFT)


root.mainloop()