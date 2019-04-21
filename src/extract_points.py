import cv2
import numpy as np 
from src.import_data import get_dataset, get_csv_training
import matplotlib.pyplot as plt
import random

def plot_canny():
    dataset, _ = get_dataset_classification_only(10)
    edges = cv2.Canny(img, 100, 200)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()

def extract_points():
    """
    Extract the points by taking -5/+5 in every direction from point center
    """
    SIZE_SPOT = 32
    features, labels = get_dataset(10000)
    index = 0
    for f, l in zip(features, labels):
        if l.classification == 0:
            continue

        f = cv2.resize(f, (f.shape[0] * 6, f.shape[1] * 6), interpolation=cv2.INTER_CUBIC)
        if l.classification == 1:
            x_spot, y_spot = round(l.X_first_spot * 6), round(l.Y_first_spot * 6)
            spot1 = f[max(1, y_spot - SIZE_SPOT):min(f.shape[1], y_spot + SIZE_SPOT), 
                max(0, x_spot - SIZE_SPOT):min(f.shape[0], x_spot + SIZE_SPOT)]
            cv2.imwrite("output/spots/" + str(index).zfill(7) + ".tiff", \
                spot1)
            index += 1
        else:
            x_spot1, y_spot1 = round(l.X_first_spot * 6), round(l.Y_first_spot * 6)
            cv2.imwrite("output/spots/" + str(index).zfill(7) + ".tiff", \
                f[max(1, y_spot1 - SIZE_SPOT):min(f.shape[1], y_spot1 + SIZE_SPOT), 
                max(0, x_spot1 - SIZE_SPOT):min(f.shape[0], x_spot1 + SIZE_SPOT)])
            x_spot2, y_spot2 = round(l.X_second_spot * 6), round(l.Y_second_spot * 6)
            cv2.imwrite("output/spots/" + str(index+1).zfill(7) + ".tiff", \
                f[max(1, y_spot2 - SIZE_SPOT):min(f.shape[1], y_spot2 + SIZE_SPOT), 
                max(0, x_spot2 - SIZE_SPOT):min(f.shape[0], x_spot2 + SIZE_SPOT)])
            index += 2

def extract_false_images():
    """
    Extract the points by taking -5/+5 in every direction from point center
    """
    SIZE_SPOT = 32
    features, labels = get_dataset(10000)
    index = 0
    for f, l in zip(features, labels):
        if l.classification == 0:
            f = cv2.resize(f, (f.shape[0] * 6, f.shape[1] * 6), interpolation=cv2.INTER_CUBIC)
            x = random.randint(SIZE_SPOT, f.shape[0] - SIZE_SPOT - 1)
            y = random.randint(SIZE_SPOT, f.shape[0] - SIZE_SPOT - 1)
            cv2.imwrite("output/false_spots/" + str(index).zfill(7) + ".tiff", \
                    f[x - SIZE_SPOT:x + SIZE_SPOT, y -SIZE_SPOT:y+SIZE_SPOT ])
            index += 1



if __name__ == "__main__":
    extract_points()
    extract_false_images()