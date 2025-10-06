from tkinter import *
from PIL import Image,ImageTk
import math
import colorsys
import tkinter.messagebox as msg

def color_wheel(size):
    radius = size//2
    image = Image.new("RGB",(size,size),(255,255,255))  
    pixels = image.load()
    
    for y in range(size):
        for x in range(size):
            dy= y - radius
            dx= x - radius
            distance = math.sqrt(dx**2 + dy**2)

            if distance <= radius:
                angle = (math.atan2(dy,dx) + math.pi)/(2 * math.pi) 
                saturation = distance/radius
                r,g,b= colorsys.hsv_to_rgb(angle,saturation,1)
                pixels[x, y] = (int(r*255),int(g*255),int(b*255))        
            else:
                pixels[x,y]= (255,255,255)

    return image

def click(event):

    x,y = event.x,event.y
    if 0<= x < Wheel_size and 0 <= y < Wheel_size:
        rgb = Wheel_image.getpixel((x,y))
        if rgb != (255,255,255):
            hex_value = '#%02x%02x%02x' % rgb
            label.config(text=(f"RGB: {rgb}\n HEX: {hex_value}"))
        else:
            msg.askyesno("Error","Wrong Input")

root  = Tk()
root.geometry("500x500")
root.title("Color Wheel")

Wheel_size = 300
Wheel_image = color_wheel(Wheel_size)
tk_image = ImageTk.PhotoImage(Wheel_image)

canvas = Canvas(width=Wheel_size,height=Wheel_size)
canvas.pack()
canvas.create_image(0,0,anchor=NW,image = tk_image)
canvas.bind("<Button-1>",click)

label = Label(text="Select your color by clicking the circle",relief=SUNKEN,font="comicsansms 16 bold",borderwidth=5)
label.pack()



root.mainloop()