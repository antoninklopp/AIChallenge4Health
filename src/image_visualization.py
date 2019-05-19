from src.import_data import get_dataset, RESIZE_FACTOR, get_data_test
import cv2
from src.image import Image
from src.read_results_yolo import read_in

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
    left_bottom_corner = (int(float(l[1]) * 24 * RESIZE_FACTOR) - int(float(l[3]) * 24 * RESIZE_FACTOR/2)\
        , int(float(l[2]) * 24 * RESIZE_FACTOR) - int(float(l[4]) * 24 * RESIZE_FACTOR/2))
    right_top_corner = (int(float(l[1]) * 24 * RESIZE_FACTOR) + int(float(l[3]) * 24 * RESIZE_FACTOR/2)\
        , int(float(l[2]) * 24 * RESIZE_FACTOR) + int(float(l[4]) * 24 * RESIZE_FACTOR/2))
    left_bottom_middle = 0
    right_top_middle = 0
    print(left_bottom_corner, right_top_corner)
    cv2.rectangle(f, left_bottom_corner, right_top_corner, (255, 0, 0), 2)
    # cv2.rectangle(f, left_bottom_middle, right_top_middle, (255, 0, 0), 2)
    return f

def visualize_results_image():
    """
    Visualize the results from the test dataset
    """
    IMAGES = 100
    results = read_in()
    test_files = get_data_test()
    for i in range(IMAGES):
        im = test_files[i]
        r = results[i]
        if r.classification == 1:
            middle = (int(float(r.X_first_spot)), int(float(r.Y_first_spot)))
            im[middle[1], middle[0]] = [255, 255, 255]
        elif r.classification == 2:
            middle = (int(float(r.X_first_spot)), int(float(r.Y_first_spot)))
            im[middle[1], middle[0]] = [255, 255, 255]
            middle2 = (int(float(r.X_second_spot)), int(float(r.Y_second_spot)))
            im[middle2[1], middle2[0]] = [255, 255, 255]
        cv2.imwrite("output_vis/test_image" + str(i) + ".jpg", im[:, :, 0])

if __name__ == "__main__":
    visualize_results_image()