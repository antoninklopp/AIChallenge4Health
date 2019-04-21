import numpy as np 
import cv2
import csv
from src.image import Image
from PIL import Image as PILmage
from skimage import io
import glob

def get_csv_training():
    list_images = []
    with open('DataChallenge/descriptions_training.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            row = row[0].split(",")
            _id, c, xf, yf, xs, ys = row
            i = Image(_id, c, xf, yf, xs, ys)
            list_images.append(i)

    return list_images

def get_data_training():
    train_data = io.imread("DataChallenge/images_training.tiff")
    return np.array(train_data)

def get_data_test():
    train_data = io.imread("DataChallenge/images_test.tiff")
    return np.array(train_data)

def export_data_tiff_to_show():
    train_data = get_data_training()
    for i, image in enumerate(train_data):
        cv2.imwrite("DataChallenge/train_individuals/" + str(i).zfill(6) + ".tiff", image)

def export_data_test_tiff():
    train_data = get_data_test()
    for i, image in enumerate(train_data):
        cv2.imwrite("DataChallenge/train_individuals_test/" + str(i).zfill(6) + ".tiff", image)

def get_dataset_classification_only(max_images):
    """
    Run first export_data_tiff_to_show before using this method
    Used to save RAM
    """
    features = []
    labels = []
    for i, t_file in enumerate(sorted(glob.glob("DataChallenge/train_individuals/*.tiff"))):
        if i < max_images:
            features.append(cv2.imread(t_file, 0))
        else:
            break

    labels = [i.classification for i in get_csv_training()[:max_images]]

    return features, labels

def get_dataset(max_images=None):
    """
    Run first export_data_tiff_to_show before using this method
    Used to save RAM
    """
    features = []
    labels = []
    for i, t_file in enumerate(sorted(glob.glob("DataChallenge/train_individuals/*.tiff"))):
        if max_images is None or i < max_images:
            features.append(cv2.imread(t_file, 0))
        else:
            break

    labels = [i for i in get_csv_training()[:max_images]]

    return features, labels

def get_dataset_test(max_images=None):
    test_files = []
    for i, t_file in enumerate(sorted(glob.glob("DataChallenge/train_individuals_test/*.tiff"))):
        if max_images is None or i < max_images:
            test_files.append(cv2.imread(t_file, 0))
        else:
            break

    return test_files

if __name__ == "__main__":
    export_data_test_tiff()