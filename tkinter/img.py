from tkinter import *
from PIL import Image, ImageTk

win_root = Tk()
win_root.title("COD") 
win_root.geometry("500x500")
 
Win = Label(text="Call Of Duty")
Win.pack()

#photo = PhotoImage(file="cod.png")
image = Image.open("tkinter\cod.png")
photo = ImageTk.PhotoImage(image)

img = Label(image=photo)

img.pack()



win_root.mainloop()