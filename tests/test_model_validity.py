from src.models.example_random_model import RandomModel
from src.answers import AbstractModel
import importlib

class TestValidity:

    def test_validity(self):
        self.validity_random_model()

    def validity_random_model(self):
        r = RandomModel()
        answers = r.evaluate_model(" ")
        assert answers is not None
        assert type(answers) == list
        assert len(answers) == 144994


if __name__ == "__main__":
    t = TestValidity()
    t.validity_one_model("RandomModel")