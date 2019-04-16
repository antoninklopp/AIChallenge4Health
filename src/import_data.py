import numpy as np 
import cv2
import csv
from src.image import Image
from PIL import Image as PILmage
from skimage import io
import glob

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

def get_dataset(max_images):
	"""
	Run first export_data_tiff_to_show before using this method
	Used to save RAM
	"""
	features = []
	labels = []
	for i, t_file in enumerate(glob.glob("DataChallenge/train_individuals/*.tiff")):
		if i < max_images:
			features.append(io.imread(t_file, as_gray=True))
		else:
			break

	labels = [i.classification for i in data_csv()[:max_images]]
	print(labels[:10])

	return features, labels


if __name__ == "__main__":
    export_data_tiff_to_show()