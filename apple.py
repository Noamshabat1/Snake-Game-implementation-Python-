
class Apple:
    COLOR = "green"

    def __init__(self, x, y, score):
        """
        the builder for the Apple class.
        :param x: the x coord for an apple.
        :param y: rhe y coord for an apple.
        :param score: the score for eating an apple.
        """
        self.__score = score
        self.__location = (x, y)

    def get_score(self):
        """
        a get method that returns the score of the game.
        :return: the score for an apple.
        """
        return self.__score

    def get_location(self):
        """
        a get method that returns the location of the apple.
        :return: the location of the apple.
        """
        return self.__location

    def get_color(self):
        return self.COLOR
