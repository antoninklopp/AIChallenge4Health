class Image:
    """
    Class containing the data of one image from the csv file : 
    descriptions_training.csv
    """

    def __init__(self, _id, _classification, _X_first_spot, _Y_first_spot, \
        _X_second_spot, _Y_second_spot):
        self.id = int(_id)
        self.classification = int(_classification)
        self.X_first_spot = float(_X_first_spot)
        self.X_second_spot = float(_X_second_spot)
        self.Y_first_spot = float(_Y_first_spot)
        self.Y_second_spot = float(_Y_second_spot)

    def first_spot(self):
        return (self.X_first_spot, self.Y_first_spot)

    def second_spot(self):
        return (self.X_second_spot, self.Y_second_spot)

    def __str__(self):
        return "Image of class : " + str(self.classification)