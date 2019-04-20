from __future__ import division
import tensorflow as tf
from src.import_data import get_dataset
import numpy as np

def get_model():

    features, labels = get_dataset(100000)
    x_train, y_train = np.array(features[:-1000]), np.array(labels[:-1000])
    x_test, y_test = np.array(features[-1000:]), np.array(labels[-1000:])

    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(24, 24)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dense(3, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

    return model, x_test, y_test