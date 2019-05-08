import cv2
import numpy 
import matplotlib.pyplot as plt
from src.image_visualization import visualize_points_one_image
from src.import_data import get_dataset, RESIZE_FACTOR

def save_hists():
    features, labels = get_dataset(1000)
    boudaries = 4 * RESIZE_FACTOR

    for i, (f, l) in enumerate(zip(features, labels)):
        plt.close()
        hist, bins, _ = plt.hist(f.flatten(), bins=[i * 10 for i in range(26)])
        # print(hist)

        if l.classification != 0:
            f = visualize_points_one_image(f, l)

        plt.subplot(211), plt.imshow(f, 'gray')
        plt.subplot(212), plt.plot(bins[:-1], hist)
        plt.xlim([0,256])

        plt.savefig("output_vis/hist" + str(i).zfill(6) + ".jpg")

if __name__ == "__main__":
    save_hists()