"""
This script is meant to create the csv for the answers to the challenge. 
"""

from src.import_data import get_dataset_test
import csv 
from abc import ABC, abstractmethod

class AbstractModel(ABC):
    """
    Every model should derive from this class
    """

    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def evaluate_model(self, data_test):
        """
        The evaluate should return the answers as follows : 
        classification, spot_1_x, spot_1_y, spot_2_x, spot_2_y
        """
        pass

    def write_answers_to_csv(self):
        """
        Writes the answers to a csv file
        """
        data_test = get_dataset_test()
        answers_model = self.evaluate_model(data_test)
        # Add the number of the test to the answers model
        for i in range(len(answers_model)):
            answers_model[i] = [str(i)] + [str(j) for j in answers_model[i]]

        with open("output/answers_" + str(self.__class__.__name__) + ".csv", 'w') as answers:
            write_answers = csv.writer(answers)
            write_answers.writerows(answers_model)

        print("Answers were written to csv")

        