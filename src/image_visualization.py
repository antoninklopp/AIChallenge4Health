from src.import_data import get_dataset, RESIZE_FACTOR
import cv2
from image import Image

def visualize_points_images():
    features, labels = get_dataset(1000)
    for index, (f, l) in enumerate(zip(features, labels)):
        if l.classification == 0:
            continue
        f = visualize_points_one_image(f, l, index)
        cv2.imwrite("output_vis/" + str(index) + ".jpg", f)

def visualize_points_one_image(f, l, index):
    boudaries = 4 * RESIZE_FACTOR
    boxes = open("DataChallenge/train_individuals/" + str(index).zfill(6) + ".txt")
    l = boxes.readline().split(" ")
    left_bottom_corner = (int(float(l[1]) * 24 * RESIZE_FACTOR), int(float(l[2]) * 24 * RESIZE_FACTOR))
    right_top_corner = (int(float(l[3]) * 24 * RESIZE_FACTOR), int(float(l[4]) * 24 * RESIZE_FACTOR))
    left_bottom_middle = 0
    right_top_middle = 0
    print(left_bottom_corner, right_top_corner)
    cv2.rectangle(f, left_bottom_corner, right_top_corner, (255, 0, 0), 2)
    # cv2.rectangle(f, left_bottom_middle, right_top_middle, (255, 0, 0), 2)
    return f

if __name__ == "__main__":
    visualize_points_images()