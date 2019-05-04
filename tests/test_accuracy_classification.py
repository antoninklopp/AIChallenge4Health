from src.import_data import get_csv_training, get_dataset, get_dataset_classification_only
from src.models.image_cnn import ImageCNN
from src.models.basic_cnn import BasicCNN
from src.calculate_metrics import calculate_metric_classification, calculate_metric
import numpy as np
from src.image import Image
from src.read_results_yolo import read_in

def classification_score():
    """
    Test the classificarion score on the basic CNN
    """
    basic = BasicCNN()
    model = basic.get_model()
    data_training, labels = get_dataset_classification_only(1000)

    evaluation = basic.evaluate_model(np.array(data_training))
    evaluation = [Image(i, np.argmax(j[0]), 0, 0, 0, 0) for i, j in enumerate(evaluation)]
    labels = [Image(i, j, 0, 0, 0, 0) for i, j in enumerate(labels)]
    metric = calculate_metric_classification(evaluation, labels)
    return metric

def classification_precision():
    """
    Test the classification precision from darknet YOLO network. 
    """
    images_yolo = read_in()
    data_training, labels = get_dataset(len(images_yolo))
    metric = calculate_metric(images_yolo, labels)
    return metric
    

if __name__ == "__main__":
    print(classification_precision())
    