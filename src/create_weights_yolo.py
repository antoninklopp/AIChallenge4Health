from src.import_data import get_dataset

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
            size_spot_X = l.X_first_spot/24.0
            if l.X_first_spot < 4.0 or l.X_first_spot > 24 - 4.0:
                size_spot_X = min(l.X_first_spot, 24-l.X_first_spot)
            size_spot_Y = l.Y_first_spot/24.0
            if l.Y_first_spot < 4.0 or l.Y_first_spot > 24 - 4.0:
                size_spot_Y = min(l.Y_first_spot, 24-l.Y_first_spot)
            info = " ".join([str(i) for i in [0, l.X_first_spot/24.0, l.Y_first_spot/24.0, size_spot_X/24.0, size_spot_Y/24.0]])
            file_yolo.write(info)
        else:
            size_spot_X = 8.0
            if l.X_first_spot < 4.0 or l.X_first_spot > 24 - 4.0:
                size_spot_X = min(l.X_first_spot, 24-l.X_first_spot)
            size_spot_Y = 8.0
            if l.Y_first_spot < 4.0 or l.Y_first_spot > 24 - 4.0:
                size_spot_Y = min(l.Y_first_spot, 24-l.Y_first_spot)
            info = " ".join([str(i) for i in [0, l.X_first_spot/24.0, l.Y_first_spot/24.0, size_spot_X/24.0, size_spot_Y/24.0]])
            file_yolo.write(info)
            file_yolo.write("\n")
            size_spot_X = 8.0
            if l.X_second_spot < 4.0 or l.X_second_spot > 24 - 4.0:
                size_spot_X = min(l.X_second_spot, 24-l.X_second_spot)
            size_spot_Y = 8.0
            if l.Y_second_spot < 4.0 or l.Y_second_spot > 24 - 4.0:
                size_spot_Y = min(l.Y_second_spot, 24-l.Y_second_spot)
            info = " ".join([str(i) for i in [0, l.X_second_spot/24.0, l.Y_second_spot/24.0, size_spot_X/24.0, size_spot_Y/24.0]])
            file_yolo.write(info)
        file_yolo.close()

if __name__ == "__main__":
    get_yolo_config()