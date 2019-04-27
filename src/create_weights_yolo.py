from src.import_data import get_dataset

def get_yolo_config():
    """
    Create a yolo config file
    """
    data_training, labels_training = get_dataset()
    for index, l in enumerate(labels_training):
        file_name = str(index).zfill(6) + '.txt'
        file_yolo = open("output_yolo/" + file_name, 'w')
        if l.classification == 0:
            continue
        elif l.classification == 1:
            info = " ".join([str(i) for i in [0, l.X_first_spot/24.0, l.X_first_spot/24.0, 10/24.0, 10/24.0]])
            file_yolo.write(info)
        else:
            info = " ".join([str(i) for i in [0, l.X_first_spot/24.0, l.Y_first_spot/24.0, 10/24.0, 10/24.0]])
            file_yolo.write(info)
            file_yolo.write("\n")
            info = " ".join([str(i) for i in [0, l.X_second_spot/24.0, l.Y_second_spot/24.0, 10/24.0, 10/24.0]])
            file_yolo.write(info)
        file_yolo.close()

if __name__ == "__main__":
    get_yolo_config()