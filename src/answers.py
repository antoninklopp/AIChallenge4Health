"""
This script is meant to create the csv for the answers to the challenge. 
"""

from src.import_data import get_data_test
import csv 
from abc import ABC, abstractmethod

class AbstractModel(ABC):
    """
    Every model should derive from this class
    """

    @abstractmethod
    def get_model(self):
        """
        Should return a model like a tensorflow model 
        or any machine learning that can evaluate the test 
        database

        :returns: model that can be evaluated in the @evaluate_model function
        """
        pass

    @abstractmethod
    def evaluate_model(self, data_test):
        """
        The evaluate should return the answers as follows : 
        classification, spot_1_x, spot_1_y, spot_2_x, spot_2_y

        :param data_test: The data to test the model on
        :type data_test: list of np.ndarray
            
        :returns: a list of answers that should have the following format :
            [classification, spot_1_x, spot_1_y, spot_2_x, spot_2_y]
        :rtype: list of list
        """
        pass

    def write_answers_to_csv(self):
        """
        Writes the answers to a csv file : output/answers_{model_name}.csv
        """
        data_test = get_data_test()
        answers_model = self.evaluate_model(data_test)
        # Add the number of the test to the answers model
        for i in range(len(answers_model)):
            answers_model[i] = [str(i)] + [str(j) for j in answers_model[i]]

        with open("output/answers_" + str(self.__class__.__name__) + ".csv", 'w') as answers:
            write_answers = csv.writer(answers)
            write_answers.writerows(answers_model)

        print("Answers were written to csv")

        