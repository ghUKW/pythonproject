import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2 as cv
import numpy as np
import os
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

xCanvasSize = 200
yCanvasSize = 200

screen = tk.Tk()
screen.title("My app")
screen.geometry("500x500")

canvas = Canvas(screen, width = xCanvasSize, height = yCanvasSize, bg="white") 
canvas.pack(pady=20)
model = load_model('.\Sieci_znaki.hdf5')


def predict(image):
    pred = model.predict_classes(image)
    print(pred)
    return pred

def pres_pred():
    for x in range(0,42):
        img = cv.imread('Meta/{0}.png'.format(x))
        img_ = cv.resize(img,(64,64))
        img_ = np.reshape(img_,[1,64,64,3])
        pred =np.argmax(model.predict(img_), axis=-1)
        print('Dla obrazka {0} klasa: {1}'.format(x,pred[0]))

def select_image():

    #load image
    filepath = filedialog.askopenfilename()
    img = Image.open(filepath)

    numpy_image=numpy.array(img)  
    print(numpy_image.shape) 
    # imread = (64,64,3)   
    opencvImage = numpy.array(img) 
    opencvImage = opencvImage[:, :, :].copy() 
    dim = (64, 64)
    opencvImage = cv.resize(opencvImage, dim, interpolation = cv.INTER_AREA)
    # print(opencvImage.shape) -> ksztalt (64, 64, 3)
    

    # Image = 200x200
    img = img.resize((xCanvasSize, yCanvasSize)) 
    imgTk = ImageTk.PhotoImage(img)
    canvas.create_image(0,0, anchor=NW, image=imgTk)
    canvas.image = imgTk 



pred=0
button = tk.Button(text="Upload image", command=select_image)
button1 = tk.Button(text="Predict", command=pres_pred)
PredLabel = tk.Label(text="Wynik predykcji")
TextPred = tk.Label(text=pred)
button.pack()
button1.pack()
PredLabel.pack()
TextPred.pack()


screen.mainloop()

