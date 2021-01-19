import matplotlib
matplotlib.use("Agg")
from pyimagesearch.trafficsignnet import TrafficSignNet
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report
from skimage import transform
from skimage import exposure
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import os
from sklearn.utils import class_weight

def load_split(basePath, csvPath):
    data = []
    labels = []
    rows = open(csvPath).read().strip().split("\n")[1:]
    random.shuffle(rows)
    for (i, row) in enumerate(rows):
        if i > 0 and i % 1000 == 0:
            print("Przetworzonych obrazków:  {} ".format(i))
        (label, imagePath) = row.strip().split(",")[-2:]
        imagePath = os.path.sep.join([basePath, imagePath])
        image = io.imread(imagePath)
        image = transform.resize(image, (32, 32))
        image = exposure.equalize_adapthist(image, clip_limit=0.1)

        data.append(image)
        labels.append(int(label))
	
    # Konwertowanie danych do tablic numpy
    data = np.array(data)
    labels = np.array(labels)
	# Zwrócenie tupli z danymi i etykietami
    return (data, labels)

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="sciezka do zbioru")
ap.add_argument("-m", "--model", required=True,
	help="sciezka do zapisania modelu")
args = vars(ap.parse_args())

NUM_EPOCHS = 30
BS = 64
# załadowanie etykiet
labelNames = open("signnames.csv").read().strip().split("\n")[1:]
labelNames = [l.split(",")[1] for l in labelNames]


trainPath = os.path.sep.join([args["dataset"], "Train.csv"])
testPath = os.path.sep.join([args["dataset"], "Test.csv"])
# wczytanie danych testowych i treningowych
(trainX, trainY) = load_split(args["dataset"], trainPath)
(testX, testY) = load_split(args["dataset"], testPath)
# Skalowanie danych do wartości [0, 1]
trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0
#Nadanie wag ze względu na ilośc danych
weight = class_weight.compute_class_weight('balanced',
                                                 np.unique(trainY),
                                                 trainY)
class_weights = {i : weight[i] for i in range(43)}
# kodowanie one-hot labeling
numLabels = len(np.unique(trainY))												 
trainY = to_categorical(trainY, numLabels)
testY = to_categorical(testY, numLabels)

classTotals = trainY.sum(axis=0)
classWeight = classTotals.max() / classTotals
aug = ImageDataGenerator(
	rotation_range=10,
	zoom_range=0.15,
	width_shift_range=0.1,
	height_shift_range=0.1,
	shear_range=0.15,
	horizontal_flip=False,
	vertical_flip=False,
	fill_mode="nearest")

# inicjalizacja optymalizatoria i kompilacji
opt = Adam(lr=1e-3, decay=1e-3 / (30 * 0.5))
model = TrafficSignNet.build(width=32, height=32, depth=3,
	classes=numLabels)
model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])

# trenowanie modelu
H = model.fit_generator(
	aug.flow(trainX, trainY, batch_size=BS),
	validation_data=(testX, testY),
	steps_per_epoch=trainX.shape[0] // BS,
	epochs=NUM_EPOCHS,
	class_weight=class_weights,
	verbose=1)

model.save(args["model"])