from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

root = Tk()
root.geometry("400x400")
root.title("Menu")

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


text=Text(root,font="comicsansms 16 ")
text.pack(fill=BOTH)

mainmenu = Menu(root)
m1 =Menu(mainmenu,tearoff=0)
m1.add_command(label="New File",command=myfun)
m1.add_separator()
m1.add_command(label="Save",command=savefile)
m1.add_command(label="Open",command=openfile)
m1.add_separator()
m1.add_command(label="Print",command=myfun)
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


root.mainloop()

