from src.answers import AbstractModel
import random


class RandomModel(AbstractModel):
    """
    A simple random model to test if the AbstractModel and the
    evaluation model is working
    """

    def __init__(self):
        print("Created a Random model class")

    def get_model(self):
        pass

    def evaluate_model(self, data_test):
        """
        144994 tests in the data set
        """
        answers = []
        for i in range(144994):
            number_points = random.randint(0, 2)
            new_answer = [number_points]
            for j in range(number_points):
                new_answer.append(random.random() * 24)
                new_answer.append(random.random() * 24)

            for j in range(2 - number_points):
                new_answer.append(0)
                new_answer.append(0)

            answers.append(new_answer)

        return answers


if __name__ == "__main__":
    r = RandomModel()
    r.write_answers_to_csv()
