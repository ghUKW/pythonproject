import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk



xCanvasSize = 300
yCanvasSize = 300

screen = tk.Tk()
screen.title("My app")
screen.geometry("500x500")


canvas = Canvas(screen, width = xCanvasSize, height = yCanvasSize, bg="white") 
canvas.pack(pady=20)

def select_image():
    filepath = filedialog.askopenfilename()
    image=Image.open(filepath)
    image = image.resize((xCanvasSize, yCanvasSize))  
    photoImage = ImageTk.PhotoImage(image)
    canvas.create_image(0,0, anchor=NW, image=photoImage)    
    canvas.image = photoImage 
   
 

button = tk.Button(text="Upload image", command=select_image)
button.pack()


screen.mainloop()

