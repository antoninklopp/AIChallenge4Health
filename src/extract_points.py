import cv2
import numpy as np 
from src.import_data import get_dataset, get_csv_training
import matplotlib.pyplot as plt

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
    SIZE_SPOT = 5
    features, labels = get_dataset(10000)
    index = 0
    for f, l in zip(features, labels):
        if l.classification == 0:
            continue
        elif l.classification == 1:
            x_spot, y_spot = round(l.X_first_spot), round(l.Y_first_spot)
            cv2.imwrite("output/spots/" + str(index).zfill(7) + ".tiff", \
                f[ 
                max(1, y_spot - SIZE_SPOT):min(f.shape[1], y_spot + SIZE_SPOT), 
                max(0, x_spot - SIZE_SPOT):min(f.shape[0], x_spot + SIZE_SPOT)])
            index += 1
        else:
            x_spot1, y_spot1 = round(l.X_first_spot), round(l.Y_first_spot)
            x_spot2, y_spot2 = round(l.X_second_spot), round(l.Y_second_spot)
            cv2.imwrite("output/spots/" + str(index) + ".tiff", \
                f[max(1, y_spot1 - SIZE_SPOT):min(f.shape[1], y_spot1 + SIZE_SPOT), 
                max(0, x_spot1 - SIZE_SPOT):min(f.shape[0], x_spot1 + SIZE_SPOT)])
            cv2.imwrite("output/spots/" + str(index+1).zfill(7) + ".tiff", \
                f[max(1, y_spot2 - SIZE_SPOT):min(f.shape[1], y_spot2 + SIZE_SPOT), 
                max(0, x_spot2 - SIZE_SPOT):min(f.shape[0], x_spot2 + SIZE_SPOT)])
            index += 2


if __name__ == "__main__":
    extract_points()