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
from skimage import transform
from skimage import exposure
from skimage import io

# rozmiar obrazka
xCanvasSize = 200
yCanvasSize = 200

# rozmiar oraz tytuł okna
screen = tk.Tk()
screen.title("Rozpoznawanie znaku")
screen.geometry("500x500")

# inicjacja okna 
canvas = Canvas(screen, width = xCanvasSize, height = yCanvasSize, bg="white") 
canvas.pack(pady=20)

print(os.getcwd())

# ładowanie modelu
# model = load_model('./pythonproject/signnet.model')
model = load_model('.\signnet.model')

# inicjacja zmiennej będącej scizka do pliku 
filepath =''

# label wynikowy
PredLabel = tk.Label(text="")

# ładowanie 
znaki = road_signs

# metoda pytająca o scieżke do pliku i jego późniejsze wyswietlenie na interfejsie 
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

# metoda słuzazca do predykcji na podstawie modelu 
def predict(imagePath):
    # wyjątek jak nie znajdzie znaku
    try:
        # przetwarzanie obrazu
        img = io.imread(imagePath)
        image = transform.resize(img, (32, 32))
        image = exposure.equalize_adapthist(image, clip_limit=0.1)
        image = image.astype("float32") / 255.0
        image = np.expand_dims(image, axis=0)
        # predykcja 
        preds = model.predict(image)
        j = preds.argmax(axis=1)[0]  
        print(znaki[str(j)])
        show_message(znaki[str(j)])
    except:
        show_message("Nie znaleziono tego znaku")

# łączenie modelu z labelem oraz jego wyświetlenie
def show_message(pred):
    print(pred)
    global PredLabel
    PredLabel.config(text="Wynik predykcji: " + pred)
    PredLabel.pack()

# buttony do interfejsu
button = tk.Button(text="Upload image", command=select_image)
buttonPredict = tk.Button(text="Predict", command=lambda : predict(filepath))

button.pack()
buttonPredict.pack()

screen.mainloop()

