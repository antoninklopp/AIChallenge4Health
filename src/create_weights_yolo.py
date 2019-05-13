from src.import_data import get_dataset, RESIZE_FACTOR, get_csv_training
import math
import cv2 

def distance(spot1, spot2):
    return math.sqrt((spot1[0] - spot2[0])**2 + (spot1[1] - spot2[1])**2)

def get_yolo_config():
    """
    Create a yolo config file
    """
    labels_training = get_csv_training()
    for index, l in enumerate(labels_training):
        if (index % 1000 == 0):
            print(index)
        file_name = str(index).zfill(6) + '.txt'
        d = cv2.imread("DataChallenge/train_individuals/" + str(index).zfill(6) + ".jpg", 0)
        file_yolo = open("DataChallenge/train_individuals/" + file_name, 'w')
        if l.classification == 0:
            continue
        elif l.classification == 1:
            size_spot_X = 8.0
            if l.X_first_spot < 4.0 or l.X_first_spot > 24 - 4.0:
                size_spot_X = min(l.X_first_spot, 24-l.X_first_spot)
            size_spot_Y = 8.0
            if l.Y_first_spot < 4.0 or l.Y_first_spot > 24 - 4.0:
                size_spot_Y = min(l.Y_first_spot, 24-l.Y_first_spot)
            info = " ".join([str(i) for i in get_yolo_bouding_box(d, l.first_spot())])
            file_yolo.write(info)
        else:
            size_spot_X = 8.0
            if l.X_first_spot < 4.0 or l.X_first_spot > 24 - 4.0:
                size_spot_X = min(l.X_first_spot, 24-l.X_first_spot) * 2
            size_spot_Y = 8.0
            if l.Y_first_spot < 4.0 or l.Y_first_spot > 24 - 4.0:
                size_spot_Y = min(l.Y_first_spot, 24-l.Y_first_spot) * 2
            info = " ".join([str(i) for i in get_yolo_bouding_box(d, l.first_spot())])
            file_yolo.write(info)
            file_yolo.write("\n")
            size_spot_X = 8.0
            if l.X_second_spot < 4.0 or l.X_second_spot > 24 - 4.0:
                size_spot_X = min(l.X_second_spot, 24-l.X_second_spot) * 2
            size_spot_Y = 8.0
            if l.Y_second_spot < 4.0 or l.Y_second_spot > 24 - 4.0:
                size_spot_Y = min(l.Y_second_spot, 24-l.Y_second_spot) * 2
            info = " ".join([str(i) for i in get_yolo_bouding_box(d, l.second_spot())])
            file_yolo.write(info)
        file_yolo.close()

def get_yolo_bouding_box(image, middle_spot, max=4*RESIZE_FACTOR):
    """
    Finds a more or less precise bouding box of a pixel
    """
    # We will find each corner one at a time
    i = int(middle_spot[0] * RESIZE_FACTOR)
    right_side = -1
    while (i < int((middle_spot[0] + 4 + 0.5) * RESIZE_FACTOR) and i < 24 * RESIZE_FACTOR):
        if image[i, int(RESIZE_FACTOR * middle_spot[1])] > 255.0/2:
            right_side = i/(24.0 * RESIZE_FACTOR)
            break
        i += 1

    if right_side == -1:
        right_side = 1

    # left side
    i = int(middle_spot[0] * RESIZE_FACTOR)
    left_side = -1
    while (i > int((middle_spot[0] - 4 - 0.5) * RESIZE_FACTOR) and i > 0):
        if image[i, int(RESIZE_FACTOR * middle_spot[1])] > 255.0/2:
            left_side = i/(24.0 * RESIZE_FACTOR)
            break
        i -= 1

    if left_side == -1:
        left_side = 0

    # top side
    j = int(middle_spot[1] * RESIZE_FACTOR)
    top_side = -1
    while (j > int((middle_spot[1] - 4 - 0.5) * RESIZE_FACTOR) and j > 0):
        if image[int(RESIZE_FACTOR * middle_spot[0]), j] > 255.0/2:
            top_side = j/(24.0 * RESIZE_FACTOR)
            break
        j -= 1

    if top_side == -1:
        top_side = 0

    # bottom side
    j = int(middle_spot[1] * RESIZE_FACTOR)
    bottom_side = -1
    while (j < int((middle_spot[1] + 4 + 0.5) * RESIZE_FACTOR) and j < 24 * RESIZE_FACTOR):
        if image[int(RESIZE_FACTOR * middle_spot[0]), j] > 255.0/2:
            bottom_side = j/(24.0 * RESIZE_FACTOR)
            break
        j += 1

    if bottom_side == -1:
        bottom_side = 1

    return [0, left_side, top_side, right_side - left_side, bottom_side - top_side]


if __name__ == "__main__":
    get_yolo_config()
    