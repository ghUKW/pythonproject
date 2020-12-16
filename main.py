import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2 as cv
import numpy 
import os
from PIL import Image, ImageTk



xCanvasSize = 200
yCanvasSize = 200

screen = tk.Tk()
screen.title("My app")
screen.geometry("500x500")


canvas = Canvas(screen, width = xCanvasSize, height = yCanvasSize, bg="white") 
canvas.pack(pady=20)


def select_image():

    #load image
    filepath = filedialog.askopenfilename()
    img = Image.open(filepath)

    #imread = (64,64,3)   
    opencvImage = numpy.array(img) 
    opencvImage = opencvImage[:, :, ::-1].copy() 
    dim = (64, 64)
    opencvImage = cv.resize(opencvImage, dim, interpolation = cv.INTER_AREA)

    # Image = 200x200
    img = img.resize((xCanvasSize, yCanvasSize)) 
    imgTk = ImageTk.PhotoImage(img)
    canvas.create_image(0,0, anchor=NW, image=imgTk)
    canvas.image = imgTk 

button = tk.Button(text="Upload image", command=select_image)
button.pack()


screen.mainloop()

