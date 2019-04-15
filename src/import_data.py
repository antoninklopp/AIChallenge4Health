import numpy as np 
import cv2
import csv
from src.image import Image

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

if __name__ == "__main__":
    train_data = cv2.imread("DataChallenge/images_training.tiff", -1)
    print(train_data.shape)
    print(len(data_csv()))