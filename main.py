import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2 as cv
import numpy as np
import os
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from signs import road_signs

xCanvasSize = 200
yCanvasSize = 200

screen = tk.Tk()
screen.title("My app")
screen.geometry("500x500")

canvas = Canvas(screen, width = xCanvasSize, height = yCanvasSize, bg="white") 
canvas.pack(pady=20)
model = load_model('.\Sieci_znaki.hdf5')

filepath =''
PredLabel = tk.Label(text="")


def select_image():
   
    global filepath
    # load image
    filepath = filedialog.askopenfilename()
    img = Image.open(filepath)
    numpy_image=np.array(img)  
    img = img.resize((xCanvasSize, yCanvasSize)) 
    imgTk = ImageTk.PhotoImage(img)
    canvas.create_image(0,0, anchor=NW, image=imgTk)
    canvas.image = imgTk 

def predict(image):
    pred = model.predict_classes(image)
    print(pred)
    return pred

def pres_pred():
    for x in range(0,42):
        img = cv.imread(filepath.format(x))
        img_ = cv.resize(img,(64,64))
        img_ = np.reshape(img_,[1,64,64,3])
        pred =np.argmax(model.predict(img_), axis=-1)
        print('Dla obrazka {0} klasa: {1}'.format(x,pred[0]))
    show_message(pred)


def show_message(pred):
    print(pred)
    global PredLabel
    PredLabel.config(text="Wynik predykcji: " + str(road_signs[str(pred)]))
    PredLabel.pack()

button = tk.Button(text="Upload image", command=select_image)
buttonPredict = tk.Button(text="Predict", command=pres_pred)

button.pack()
buttonPredict.pack()

screen.mainloop()

