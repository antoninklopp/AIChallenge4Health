from src.import_data import get_csv_training, get_dataset, get_dataset_classification_only
from src.models.image_cnn import ImageCNN
from src.models.basic_cnn import BasicCNN
from src.calculate_metrics import calculate_metric_classification, calculate_metric
import numpy as np
from src.image import Image
from src.read_results_yolo import read_in

def output():
    """
    Test the classification precision from darknet YOLO network. 
    """
    images_yolo = read_in()
    images_str = []
    for image in images_yolo:
        images_str.append(image.to_csv())
        
    with open("output/answers_" + str(self.__class__.__name__) + ".csv", 'w') as answers:
        write_answers = csv.writer(answers)
        write_answers.writerows(answers_model)
    

if __name__ == "__main__":
    print(output())