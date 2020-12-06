import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk


screen = tk.Tk()
screen.title("My app")
screen.geometry("500x500")


canvas = Canvas(screen, width = 300, height = 300, bg="white") 
canvas.pack(pady=20)

#img = PhotoImage(file='C:/Users/Aleksander/Desktop/pythonproject/Untitled.png')  
#image_id = canvas.create_image(0, 0, anchor=NW, image=img)


def select_image():
    filepath = filedialog.askopenfilename()
    img = ImageTk.PhotoImage(Image.open(filepath))     
    canvas.create_image(20,20, anchor=NW, image=img)    
    canvas.image = img 
   
 



button = tk.Button(text="Upload image", command=select_image)
button.pack()




screen.mainloop()

