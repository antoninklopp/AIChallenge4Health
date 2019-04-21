import tensorflow as tf
import tensorflow.keras as keras
try:
    from keras.models import Sequential
    from keras.layers.core import Flatten, Dense, Dropout
    from keras.layers.convolutional import Conv2D, MaxPooling2D, ZeroPadding2D
    from keras.optimizers import SGD
except ImportError:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import SGD
from src.answers import AbstractModel
from src.extract_points import get_unique_spots_labeled
from random import shuffle
import numpy as np 

class ImageCNN(AbstractModel):

    def __init__(self):
        pass

    def get_model(self):
        dataset = list(get_unique_spots_labeled(10000))
        shuffle(dataset)
        imgs = []
        labels = []
        for img, label in dataset:
            print(label)
            imgs.append(img)
            labels.append(label)

        imgs = np.array(imgs)
        print(imgs.shape)

        model = self.get_VGG_16(dataset[0][0].shape[0])
        
        model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

        imgs = np.array(imgs)
        model.fit(imgs, labels, epochs=5)

        return model

    def evaluate_model(self, data_test):
        pass

    def get_VGG_16(self, input_size):
        model = Sequential()

        model.add(ZeroPadding2D((1,1),input_shape=(input_size,input_size, 1)))
        model.add(Conv2D(input_size, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(input_size, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2), data_format="channels_first"))

        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2), data_format="channels_first"))

        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(256, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(256, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(256, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2), data_format="channels_first"))

        model.add(Flatten())
        model.add(Dense(256, activation=tf.nn.relu))
        model.add(Dense(2, activation='softmax'))

        return model