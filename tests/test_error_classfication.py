from src.calculate_metrics import score_one_image
from src.read_results_yolo import read_in
from src.import_data import get_csv_training, get_dataset, get_dataset_classification_only

THRESHOLD_ERROR = 0.4

def find_far_images():
    images_yolo = read_in()
    data_training, labels = get_dataset(len(images_yolo))
    for i, (answer, truth) in enumerate(zip(images_yolo, labels)):
        s = score_one_image(answer, truth)
        if s > THRESHOLD_ERROR:
            print("image", i, "error : ", s)
            print(answer)
            print(truth, "\n")

if __name__ == "__main__":
    find_far_images()