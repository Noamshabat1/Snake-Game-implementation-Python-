class Bomb:
    BOMB_COLOR = "red"
    WAVE_COLOR = "orange"

    def __init__(self, x, y, radius, time):
        """
        the builder for the Bomb class.
        :param x: the x coord for a bomb.
        :param y: rhe y coord for a bomb.
        :param radius: the explosion radius
        :param time: the time of the bomb before exploding.
        """
        self.__timer = time
        self.__radius = radius
        self.__location = (x, y)
        self.temp_r = -1
        self.dead = False

    def reset(self, location, radius, time):
        """
        a method that resets the boom activities.
        :param location: the new location for the bomb.
        :param radius: the radius of the wave of the explosion.
        :param time: the timer for the bomb before exploding.
        :return: None
        """
        self.__location = location
        self.__radius = radius
        self.__temp_r = -1
        self.__timer = time

    def get_dead_status(self):
        return self.dead

    def get_time(self):
        """
        a get method that returns the time of the bomb before exploding.
        :return: the time for the bomb.
        """
        return self.__timer

    def get_radius(self):
        """
        a get method that returns the radius of the bomb explosion.
        :return: the radius of the bomb.
        """
        return self.__radius

    def get_location(self):
        """
        a get method that returns the location of the bomb.
        :return: the location of the bomb.
        """
        return self.__location

    def get_color(self):
        """
        a get method that returns the color of the bomb before OR after exploding.
        :return: the color of the bomb.
        """
        return self.BOMB_COLOR if self.__timer > 0 else self.WAVE_COLOR

    def singel_turn(self):
        """
        a method that creates a single round for the bomb explosion.
        :return: True if the has stopped exploding OR False if it hasn't stopped.
        """
        if self.__timer > 0:
            self.__timer -= 1
        if self.__timer <= 0:
            self.temp_r += 1
        if self.__radius <= self.temp_r:
            self.dead = True
            return False
        return True

    def explosion(self):
        """
        a method that cole ever turn to a method that draws the bomb explosion.
        :return: None.
        """
        if self.__timer == 0:
            self.explosion_drew_for_single_turn()

    def explosion_drew_for_single_turn(self):
        """
        a method that returns the drew of the bomb explosion in each turn.
        :return: the drew of the explosion.
        """
        explosion_ls = []
        min_point = (
            self.__location[0] - self.temp_r, self.__location[1] - self.temp_r)
        for x_coord in range(min_point[0], min_point[0] + 2 * self.temp_r + 1):
            for y_coord in range(min_point[1],
                                 min_point[1] + 2 * self.temp_r + 1):
                if abs(self.__location[0] - x_coord) + abs(
                        self.__location[1] - y_coord) == self.temp_r:
                    explosion_ls.append((x_coord, y_coord))
        return explosion_ls

    def get_coordinates(self):
        if self.__timer > 0:
            return [self.__location]
        else:
            return self.explosion_drew_for_single_turn()
