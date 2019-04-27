from src.import_data import get_csv_training, get_dataset, get_dataset_classification_only
from src.models.image_cnn import ImageCNN
from src.models.basic_cnn import BasicCNN
from src.calculate_metrics import calculate_metric_classification
import numpy as np
from src.image import Image

def test_classification_score():
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
    

if __name__ == "__main__":
    print(test_classification_score())