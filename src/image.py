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
        """
        :returns: first spot of the image if it exists or (0, 0) if not
        :rtype: tuple of size 2
        """
        return (self.X_first_spot, self.Y_first_spot)

    def second_spot(self):
        """
        :returns: second spot of the image if it exists or (0, 0) if not
        :rtype: tuple of size 2
        """
        return (self.X_second_spot, self.Y_second_spot)

    def __str__(self):
        returnString = "Image of class : " + str(self.classification)
        if self.classification == 0:
            return returnString
        else:
            returnString += "\nFirst spot : " + str(self.first_spot())
            if self.classification == 1:
                return returnString
            returnString += "\nSecond spot : " + str(self.second_spot())
        return returnString
        
    def to_csv(self):
        """
        Returns the string to print to the csv file
        """
        return " ".join([str(self.id), self.X_first_spot, self.Y_first_spot, self.X_second_spot, self.Y_second_spot])
