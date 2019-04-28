import numpy as np 
import cv2
import csv
from src.image import Image
from skimage import io
import glob
import scipy

RESIZE_FACTOR=5


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
        cv2.imwrite("DataChallenge/train_individuals/" + str(i).zfill(6) + ".jpg", augment_contrast(image))

def augment_contrast(image):
    """
    We choose to augment the contrast on the images simply by multiplying the 
    values of the image by a certain number. 

    Because the values of points are very low, we are sure that we will not 
    destroy 
    """
    MULTIPLE = 3
    x, y, z = np.where(image > 255/3)
    xx, yy, zz = np.where(image <= 255/MULTIPLE)
    image[x, y, z] = 255
    image[xx, yy, zz] = image[xx, yy, zz] * MULTIPLE
    image = cv2.resize(image, (image.shape[0] * RESIZE_FACTOR, image.shape[1] * RESIZE_FACTOR), interpolation=cv2.INTER_CUBIC)
    # image = scipy.signal.medfilt(image, 5)
    return image

def export_data_test_tiff():
    train_data = get_data_test()
    for i, image in enumerate(train_data):
        cv2.imwrite("DataChallenge/train_individuals_test/" + str(i).zfill(6) + ".jpg", image)

def get_dataset_classification_only(max_images):
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
    export_data_tiff_to_show()
