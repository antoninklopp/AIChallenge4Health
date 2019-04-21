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
import cv2
from src.extract_points import SIZE_SPOT, RESIZE_FACTOR
from src.models.basic_cnn import BasicCNN
import math
from src.import_data import get_dataset_test
import os

MODEL_PATH = "models/image_cnn.h5"

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) 

class ImageCNN(AbstractModel):

    def __init__(self):
        pass

    def get_model(self):
        if os.path.isfile(MODEL_PATH):
            new_model = tf.keras.models.load_model(MODEL_PATH)
            print("Loaded Image CNN model")
            return new_model

        dataset = list(get_unique_spots_labeled(10000))
        shuffle(dataset)
        imgs = []
        labels = []
        index = 0
        for img, label in dataset:
            cv2.imwrite("test_output/" + str(index) + "_" + str(label) + ".tiff", img * 255)
            imgs.append(img)
            labels.append(label)
            index += 1

        imgs = np.array(imgs)

        model = self.get_VGG_16(dataset[0][0].shape[0])
        
        model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

        imgs = np.array(imgs)
        model.fit(imgs, labels, epochs=1)

        model.save(MODEL_PATH)

        return model

    def evaluate_model(self, data_test):

        answers = []

        model = self.get_model()
        b = BasicCNN()
        model_classification = b.get_model()
        print("Loaded classification CNN")

        for image in data_test:
            label = model_classification.predict(np.array([image]))
            classification = np.argmax(label[0])
            print(classification)
            # If 0 spots, we return that there is 0 spots
            if classification == 0:
                answers.append([0, 0, 0, 0, 0])
                continue
            image = cv2.resize(image, (image.shape[0] * RESIZE_FACTOR, image.shape[1] * RESIZE_FACTOR), interpolation=cv2.INTER_CUBIC)
            max_probabilities = []
            for i in range(SIZE_SPOT, image.shape[0] - SIZE_SPOT):
                for j in range(SIZE_SPOT, image.shape[1] - SIZE_SPOT):
                    sub_image = image[i - SIZE_SPOT:i+SIZE_SPOT, j-SIZE_SPOT:j+SIZE_SPOT]
                    sub_image = np.array(sub_image) / 255.0
                    sub_image = sub_image.reshape((sub_image.shape[0], sub_image.shape[1], 1))
                    answer = model.predict(np.array([sub_image]))
                    if answer[0][1] > 0.9:
                        max_probabilities.append((i, j, answer[0][1]))

            # If only one spot, we take the max probability point
            if classification == 1:
                max_prob = max(max_probabilities, key=lambda x : x[2])
                # x and y are reverse
                answer = [1, max_prob[1]/float(RESIZE_FACTOR), max_prob[0]/float(RESIZE_FACTOR), 0, 0]
                answers.append(answer)
                print(answer)
                continue

            # If two spots
            max_probabilities.sort(key= lambda x: x)
            max_prob = max_probabilities.pop(-1)
            max_prob = (max_prob[0], max_prob[1])
            max_prob2 = None
            for p in reversed(max_probabilities):
                if distance((max_prob[0], max_prob[1]), (p[0], p[1])) > SIZE_SPOT:
                    max_prob2 = (p[0], p [1])

            if max_prob2 is None:
                max_prob2 = (0, 0)
            answer = [2, max_prob[1]/float(RESIZE_FACTOR), max_prob[0]/float(RESIZE_FACTOR), \
                max_prob2[1]/float(RESIZE_FACTOR), max_prob2[0]/float(RESIZE_FACTOR)]
            answers.append(answer)
            print(answer)


        return answers

    def get_VGG_16(self, input_size):
        model = Sequential()

        model.add(ZeroPadding2D((1,1),input_shape=(input_size,input_size, 1)))
        model.add(Conv2D(input_size, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(input_size, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2), data_format="channels_last"))

        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2), data_format="channels_last"))

        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(256, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(256, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(256, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2), data_format="channels_last"))

        model.add(Flatten())
        model.add(Dense(256, activation=tf.nn.relu))
        model.add(Dense(2, activation='softmax'))

        return model


if __name__ == "__main__":
    i = ImageCNN()
    datatest = get_dataset_test()
    print("Loaded data set to test")
    i.evaluate_model(datatest)