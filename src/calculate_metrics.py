import math
from src.image import Image

D = 2

def score_distance(spot1, spot2):
    """
    Defines the distance between two spots

    :param spot1: the first spot
    :type: tuple

    :param spot2: the second spot
    :type: tuple

    :returns: the distance
    :rtype: float
    """
    d = Math.sqrt((spot2[0] - spot1[0]) **2 + (spot2[1] - spot1[1]) **2)
    if d < D:
        return d
    else:
        return 1

def calculate_metric(list_answers, list_true):
    """

    Calculates the metric used by the online algorithm to test 
    the precision of the predictions

    :param list_answers: List of answers given by the algorithm
    :type: list of Images

    :param list_true: the list of true value corresponding to @list_answers
    :type: list of Images

    :returns: a score between 0 and 1. 
    0 means every value was perfectly predected
    1 means every value was wrongly predicted
    :rtype: float between 0 and 1
    """
    # Number of images with 0 point
    images_0 = 0
    score_0 = 0
    # Number of images with 1 point
    images_1 = 0
    score_1 = 0
    # Number of images with 2 points
    images_2 = 0
    score_2 = 0
    for answer, truth in zip(list_answers, list_true):
        if truth.classification == 0:
            if answer.classification != 0:
                score_0 += 1
            image_0 += 1
        elif truth.classification == 1:
            if answer.classification == 0:
                score_1 += 1
            elif answer.classification == 1:
                score_1 += distance(truth.first_spot(), answer.first_spot())
            else:
                score_1 += (1 + min(distance(truth.first_spot(), answer.first_spot()), \
                    distance(truth.first_spot(), answer.second_spot())))/2
            images_1 += 1
        else:
            if answer.classification == 0:
                score_2 += 1
            elif answer.classification == 1:
                score_2 += (1 + min(distance(truth.first_spot(), answer.first_spot()), \
                    distance(truth.second_spot(), answer.first_spot())))/2
            else:
                score_2 += min(distance(truth.first_spot(), answer.first_spot()), \
                    distance(truth.second_spot(), answer.first_spot()), \
                    distance(truth.first_spot(), answer.second_spot()), \
                    distance(truth.first_spot(), answer.second_spot()))
            images_2 += 1

    score_0 = score_0/float(images_0)
    score_1 = score_1/float(images_1)
    score_2 = score_2/float(images_2)

    return 0.2 * score_0 + 0.5 * score_1 * 0.3 * score_2

