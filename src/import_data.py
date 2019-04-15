import numpy as np 
import cv2
import csv
from src.image import Image
from PIL import Image as PILmage
from skimage import io

def data_csv():
    list_images = []
    with open('DataChallenge/descriptions_training.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            row = row[0].split(",")
            _id, c, xf, yf, xs, ys = row
            i = Image(_id, c, xf, yf, xs, ys)
            list_images.append(i)

    return list_images

def data_tiff():
    train_data = io.imread("DataChallenge/images_training.tiff")
    return np.array(train_data)

def export_data_tiff_to_show():
    train_data = data_tiff()
    for i, image in enumerate(train_data):
        cv2.imwrite("DataChallenge/train_individuals/" + str(i) + ".tiff", image)

if __name__ == "__main__":
    export_data_tiff_to_show()