from src.models.example_random_model import RandomModel
from src.answers import AbstractModel
import importlib

class TestValidity:

    def test_validity(self):
        self.validity_random_model()

    def validity_random_model(self):
        """
        Test the validity of the random model
        defined in src/models/example_random_model.py
        """
        r = RandomModel()
        answers = r.evaluate_model([0] * 100)
        assert answers is not None
        assert type(answers) == list
        assert len(answers) == 100


if __name__ == "__main__":
    t = TestValidity()
    t.validity_one_model("RandomModel")