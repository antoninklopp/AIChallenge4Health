from src.import_data import get_dataset, RESIZE_FACTOR
import cv2
from image import Image

def visualize_points_one_image():
    features, labels = get_dataset(1000)
    boudaries = 4 * RESIZE_FACTOR
    for index, (f, l) in enumerate(zip(features, labels)):
        if l.classification == 0:
            continue
        left_bottom_corner = (int(l.first_spot()[0] * RESIZE_FACTOR) - boudaries, \
            int(l.first_spot()[1] * RESIZE_FACTOR) - boudaries)
        right_top_corner = (int(l.first_spot()[0] * RESIZE_FACTOR) + boudaries, \
            int(l.first_spot()[1] * RESIZE_FACTOR) + boudaries)
        left_bottom_middle = (int(l.first_spot()[0] * RESIZE_FACTOR) - 1, \
            int(l.first_spot()[1] * RESIZE_FACTOR) - 1)
        right_top_middle = (int(l.first_spot()[0] * RESIZE_FACTOR) + 1, \
            int(l.first_spot()[1] * RESIZE_FACTOR) + 1)
        cv2.rectangle(f, left_bottom_corner, right_top_corner, (255, 0, 0), 2)
        cv2.rectangle(f, left_bottom_middle, right_top_middle, (255, 0, 0), 2)
        cv2.imwrite("output_vis/" + str(index) + ".jpg", f)

if __name__ == "__main__":
    visualize_points_one_image()