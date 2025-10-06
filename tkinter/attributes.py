from tkinter import *

win_root = Tk()
win_root.title("Cutie")
win_root.geometry("500x500")

win_rootlable =Label(text=''' Tkinter is a binding to the Tk GUI toolkit for Python.
It is the standard Python interface to the Tk GUI toolkit,
and is Python's de facto standard GUI.
Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python.'''
, bg="black" , fg="white" , font="comicsansms 19 bold", relief=SUNKEN, padx=120, pady=120 ,borderwidth=3)


win_rootlable.pack(side=LEFT,fill=Y)

win_root.mainloop()