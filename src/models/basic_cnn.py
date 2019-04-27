from __future__ import division
import tensorflow as tf
from src.import_data import get_dataset_classification_only
import numpy as np
from src.answers import AbstractModel
import os

MODEL_PATH = "models/basic_cnn.h5"

class BasicCNN(AbstractModel):
    """
    Simple basic CNN to find the number of points in the image. 
    """

    def get_model(self):
        if os.path.isfile(MODEL_PATH):
            new_model = tf.keras.models.load_model(MODEL_PATH)
            print("Loaded Basic CNN model")
            return new_model

        features, labels = get_dataset_classification_only(500000)
        print("Loaded dataset classification only")
        x_train, y_train = np.array(features), np.array(labels)

        x_train = x_train / 255.0

        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(24, 24)),
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense(3, activation=tf.nn.softmax)
        ])

        model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

        model.fit(x_train, y_train, epochs=5)

        model.save(MODEL_PATH)

        return model

    def evaluate_model(self, data_test):
        model = self.get_model()
        answers = model.predict(data_test)
        answers_final = []
        for i in answers:
            new_answer = [i, 0, 0, 0, 0]
            answers_final.append(new_answer)

        return answers_final

if __name__ == "__main__":
    b = BasicCNN()
    b.get_model()

