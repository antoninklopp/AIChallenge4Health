from src.image import Image
from src.calculate_metrics import calculate_metric, calculate_metric_classification
import random

class TestMetric:

    def create_randomImages(self, number):
        images = []
        for i in range(number):
            classification = random.randint(0, 2)
            if classification == 0:
                images.append(Image(i, 0, 0, 0, 0, 0))
            elif classification == 1:
                images.append(Image(i, 1, random.random() * 24, random.random() * 24, 0, 0))
            else:
                images.append(Image(i, 1, random.random() * 24, random.random() * 24, \
                    random.random() * 24, random.random() * 24))

        return images

    def create_0_images(self, number):
        images = []
        for i in range(number):
            images.append(Image(i, 0, 0, 0, 0, 0))
        return images

    def create_1_images(self, number):
        images = []
        for i in range(number):
            images.append(Image(i, 1, random.random() * 24, random.random() * 24, 0, 0))
        return images

    def create_2_images(self, number):
        images = []
        for i in range(number):
            images.append(Image(i, 2, random.random() * 24, random.random() * 24, \
                random.random() * 24, random.random() * 24))
        return images

    def test_equality(self):
        images = self.create_randomImages(10)
        images += self.create_0_images(1)
        images += self.create_1_images(1)
        images += self.create_2_images(1)
        assert calculate_metric(images, images) == 0

    def test_all_different(self):
        images_0 = self.create_0_images(10)
        images_1 = self.create_1_images(10)
        assert calculate_metric(images_0, images_1) == 1
        images_2 = self.create_2_images(10)
        assert calculate_metric(images_0, images_2) == 1

    def test_classification(self):
        images_0 = self.create_0_images(10)
        assert calculate_metric_classification(images_0, images_0) == 0
        images_1 = self.create_1_images(10)
        assert calculate_metric_classification(images_1, images_1) == 0
        images_2 = self.create_2_images(10)
        assert calculate_metric_classification(images_2, images_2) == 0


if __name__ == "__main__":
    t = TestMetric()
    t.test_equality()
    t.test_all_different()
    t.test_classification()
    