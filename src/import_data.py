import numpy as np 
import cv2
import csv
from src.image import Image
from skimage import io
import glob


def get_csv_training():
    """
    Get the annotations for
    all images contained in a particular
    csv file
    :return: list of all the annotations (id, c ???, x coordinate of the
    first spot, y coordinate of the first sport and then the coordinates
    of the second spot).
    """
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
    """
    Gets all the training images
    in the database and puts them into an array.
    :return: all the training images in the database
    :rtype: numpy.ndarray
    """
    train_data = io.imread("DataChallenge/images_training.tiff")
    return np.array(train_data)


def get_data_test():
    """
    Gets all the test images
    in the database and puts them into an array.
    :return: all the test images in the database
    :rtype: numpy.ndarray
    """
    train_data = io.imread("DataChallenge/images_test.tiff")
    return np.array(train_data)


def export_data_tiff_to_show():
    """
    Writes the training data to
    DataChallenge/train_individuals/ folder
    """
    train_data = get_data_training()
    for i, image in enumerate(train_data):
        cv2.imwrite("DataChallenge/train_individuals/" + str(i).zfill(6) + ".tiff", image)


def get_dataset(max_images):
    """
    Run first export_data_tiff_to_show before using this method
    Used to save RAM
    :param max_images: Tells how many images
    should be loaded
    :type max_images: int
    :returns: tuple of the features and their corresponding
    labels
    :rtype: tuple
    """
    features = []
    labels = []
    for i, t_file in enumerate(sorted(glob.glob("DataChallenge/train_individuals/*.tiff"))):
        if i < max_images:
            features.append(cv2.imread(t_file, 0))
        else:
            break

    labels = [i.classification for i in get_csv_training()[:max_images]]
    print(labels[:10])

    return features, labels


if __name__ == "__main__":
    export_data_tiff_to_show()