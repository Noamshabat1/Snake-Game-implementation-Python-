class Snake:
    def __init__(self):
        """
        This function initializing the snake
        """
        self.__snake = [(10, 8), (10, 9), (10, 10)]
        self.__current_direction = "Up"
        self.__head = self.__snake[-1]
        self.__tail = self.__snake[0]
        self.__color = "black"
        self.__counter = 0

    def get_counter(self):
        """
        This function returns the snake counter
        :return: Int
        """
        return self.__counter

    def plus_counter(self):
        """
        This function add 3 to the snake counter
        :return: None
        """
        self.__counter += 3

    def minus_counter(self):
        """
        This function reduce 1 from the snake counter
        :return: None
        """
        self.__counter -= 1

    def change_direction(self, direction):
        """
        This function changes the current direction of the snake
        :param direction: A string that representing the movement direction of the snake
        :return: None
        """
        self.__current_direction = direction

    def get_direction(self):
        """
        This function returns the current direction of the snake
        :return: A string that representing the movement direction of the snake
        """
        return self.__current_direction

    def move_snake(self):
        """
        This function changes the coordinates of the snake according to his movement
        :return: None
        """
        if self.__current_direction == "Up":
            self.__snake.append((self.__head[0], self.__head[1] + 1))
            if self.__counter == 0:
                self.__snake.remove(self.__tail)

        elif self.__current_direction == "Down":
            self.__snake.append((self.__head[0], self.__head[1] - 1))
            if self.__counter == 0:
                self.__snake.remove(self.__tail)

        elif self.__current_direction == "Right":
            self.__snake.append((self.__head[0] + 1, self.__head[1]))
            if self.__counter == 0:
                self.__snake.remove(self.__tail)

        elif self.__current_direction == "Left":
            self.__snake.append((self.__head[0] - 1, self.__head[1]))
            if self.__counter == 0:
                self.__snake.remove(self.__tail)
        self.__head = self.__snake[-1]
        self.__tail = self.__snake[0]

    def get_coordinates(self):
        """
        This function returns the snake coordinates
        :return: List of tuples that representing the snake coordinates
        """
        return self.__snake

    def get_location(self):
        """
        This function return the snake location (according to his head location)
        :return: A tuple of (x, y) representing the coordinates of the snakes head
        """
        return self.__head

    def is_valid_move(self, direction):
        """
        This function checks if it is possible to move in the direction of movement that the user wants
        :param direction: A string representing the movement direction
        :return: True if possible, False otherwise
        """
        if direction == "Up" and self.__current_direction == "Down":
            return False
        elif direction == "Down" and self.__current_direction == "Up":
            return False
        elif direction == "Right" and self.__current_direction == "Left":
            return False
        elif direction == "Left" and self.__current_direction == "Right":
            return False
        else:
            return True

    def get_color(self):
        """
        This function returns
        :return:
        """
        return self.__color

    def eat_apple(self):
        pass

    def get_head(self):
        return self.__head
