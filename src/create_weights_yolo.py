from src.import_data import get_dataset
import math

def distance(spot1, spot2):
    return math.sqrt((spot1[0] - spot2[0])**2 + (spot1[1] - spot2[1])**2)

def get_yolo_config():
    """
    Create a yolo config file
    """
    data_training, labels_training = get_dataset()
    for index, l in enumerate(labels_training):
        file_name = str(index).zfill(6) + '.txt'
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
            info = " ".join([str(i) for i in [0, l.X_first_spot/24.0, l.Y_first_spot/24.0, size_spot_X/24.0, size_spot_Y/24.0]])
            file_yolo.write(info)
        else:
            if distance(l.first_spot(), l.second_spot()) < 8.0:
                size_spot_X = 8.0
                if l.X_first_spot < 4.0 or l.X_first_spot > 24 - 4.0:
                    size_spot_X = min(l.X_first_spot, 24-l.X_first_spot) * 2
                size_spot_Y = 8.0
                if l.Y_first_spot < 4.0 or l.Y_first_spot > 24 - 4.0:
                    size_spot_Y = min(l.Y_first_spot, 24-l.Y_first_spot) * 2
                info = " ".join([str(i) for i in [1, l.X_first_spot/24.0, l.Y_first_spot/24.0, size_spot_X/24.0, size_spot_Y/24.0]])
                file_yolo.write(info)
                file_yolo.write("\n")
                size_spot_X = 8.0
                if l.X_second_spot < 4.0 or l.X_second_spot > 24 - 4.0:
                    size_spot_X = min(l.X_second_spot, 24-l.X_second_spot) * 2
                size_spot_Y = 8.0
                if l.Y_second_spot < 4.0 or l.Y_second_spot > 24 - 4.0:
                    size_spot_Y = min(l.Y_second_spot, 24-l.Y_second_spot) * 2
                info = " ".join([str(i) for i in [1, l.X_second_spot/24.0, l.Y_second_spot/24.0, size_spot_X/24.0, size_spot_Y/24.0]])
                file_yolo.write(info)
            else:
                size_spot_X = 8.0
                if l.X_first_spot < 4.0 or l.X_first_spot > 24 - 4.0:
                    size_spot_X = min(l.X_first_spot, 24-l.X_first_spot) * 2
                size_spot_Y = 8.0
                if l.Y_first_spot < 4.0 or l.Y_first_spot > 24 - 4.0:
                    size_spot_Y = min(l.Y_first_spot, 24-l.Y_first_spot) * 2
                info = " ".join([str(i) for i in [0, l.X_first_spot/24.0, l.Y_first_spot/24.0, size_spot_X/24.0, size_spot_Y/24.0]])
                file_yolo.write(info)
                file_yolo.write("\n")
                size_spot_X = 8.0
                if l.X_second_spot < 4.0 or l.X_second_spot > 24 - 4.0:
                    size_spot_X = min(l.X_second_spot, 24-l.X_second_spot) * 2
                size_spot_Y = 8.0
                if l.Y_second_spot < 4.0 or l.Y_second_spot > 24 - 4.0:
                    size_spot_Y = min(l.Y_second_spot, 24-l.Y_second_spot) * 2
                info = " ".join([str(i) for i in [0, l.X_second_spot/24.0, l.Y_second_spot/24.0, size_spot_X/24.0, size_spot_Y/24.0]])
                file_yolo.write(info)
        file_yolo.close()

if __name__ == "__main__":
    get_yolo_config()