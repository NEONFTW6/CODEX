from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import tkinter.messagebox as msg
import os


root = Tk()
root.geometry("400x400")
root.title("NOTE EDITOR")

def prin():
 file=askopenfilename()
 if file:
   os.startfile(file,"print")
   
def myfun():
 print("HELLOOO")  

def savefile():
 file= asksaveasfilename(defaultextension=".txt",filetypes=[("Textfile","*.txt")])

 if file:
    content = text.get("1.0",END)
 with open(file, "w") as f:
    f.write(content)
    print("File Saved")

def openfile():
 file= askopenfilename(defaultextension=".txt",filetypes=[("Textfile","*.txt"),("All files","*.")])

 if file:
 
  with open(file, "r") as f:
    content= f.read()
    text.delete("1.0", END)         
    text.insert("1.0", content)     
    print(f"File Opened{file}")

def help():
  ms= msg.askyesno("Help","Do you need help?")
  if ms==YES:
     msg.showinfo("Help","Go to Refresh menu and try to refresh!")
  else:
    msg.showinfo("Help","Thank you for cooperating")

def refres():
  ms1=msg.askokcancel("Refresh","Are you sure you want to refresh!")
  if ms1==YES:
    text.delete("1.0",END)
    msg.showinfo("Rfresh","Operation Success") 
  elif ms1==NO:
     msg.showinfo("Refresh","Thank you for cooperating!")

def new(): 
    text.delete("1.0",END)
    
 
text=Text(root,font="comicsansms 16 ")
text.pack(fill=BOTH)

mainmenu = Menu(root)
m1 =Menu(mainmenu,tearoff=0)
m1.add_command(label="New File",command=new)
m1.add_separator()
m1.add_command(label="Save",command=savefile)
m1.add_command(label="Open",command=openfile)
m1.add_separator()
m1.add_command(label="Print",command=prin)
m1.add_command(label="Exit",command=quit)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2 = Menu(mainmenu)
m2 =Menu(mainmenu,tearoff=0)
m2.add_command(label="Copy",command=myfun)
m2.add_command(label="Cut",command=myfun)
m2.add_separator()
m2.add_command(label="Find",command=myfun)
m2.add_command(label="Exit",command=quit)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainmenu)
m3 =Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Refresh",command=refres)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Setting",menu=m3)


root.mainloop()

