import game_parameters as gp
from apple import Apple
from bomb import Bomb
from snake import Snake


class Game:

    def __init__(self):
        self.score = 0
        self.game_is_over = False
        self.snake = Snake()
        self.apples = []
        self.bomb = None
        self.bomb = self.create_bomb()
        for i in range(3):
            self.apples.append(self.create_apple())

    def get_snake_direction(self):
        return self.snake.get_direction()

    def create_bomb(self):
        x, y, radius, time = gp.get_random_bomb_data()
        while not self.legal_coordinate((x, y)):
            x, y, radius, time = gp.get_random_bomb_data()

        return Bomb(x, y, radius, time)

    def create_apple(self):
        x, y, score = gp.get_random_apple_data()
        while not self.legal_coordinate((x, y)):
            x, y, score = gp.get_random_apple_data()

        return Apple(x, y, score)

    def get_colored_coordinates(self):
        colored_coordinates = []
        for coordinate in self.snake.get_coordinates():
            colored_coordinates.append(
                (coordinate[0], coordinate[1], self.snake.get_color()))
        for apple in self.apples:
            coordinate = apple.get_location()
            colored_coordinates.append(
                (coordinate[0], coordinate[1], apple.get_color()))
        for coordinate in self.bomb.get_coordinates():
            colored_coordinates.append(
                (coordinate[0], coordinate[1], self.bomb.get_color()))

        finel_coords = []
        for coord in colored_coordinates:
            if coord[0] < gp.WIDTH and coord[1] < gp.HEIGHT and coord[
                0] >= 0 and coord[1] >= 0:
                finel_coords.append(coord)

        return finel_coords

    def get_coordinates(self):
        coordinates = []
        for coordinate in self.snake.get_coordinates():
            coordinates.append(coordinate)
        for apple in self.apples:
            coordinates.append(apple.get_location())
        if self.bomb is not None:
            for coordinate in self.bomb.get_coordinates():
                coordinates.append(coordinate)
        return coordinates

    def is_over(self):
        return self.game_is_over

    def get_score(self):
        return self.score

    def legal_coordinate(self, coordinate):
        if coordinate[0] >= gp.WIDTH or coordinate[1] >= gp.HEIGHT:
            return False
        if coordinate[0] < 0 or coordinate[1] < 0:
            return False
        if coordinate in self.get_coordinates():
            return False
        return True

    def single_turn(self, direction):
        if self.snake.is_valid_move(direction):
            self.snake.change_direction(direction)
        self.snake.move_snake()
        if self.snake.get_counter() > 0:
            self.snake.minus_counter()
        if self.check_eat_apple():
            self.snake.plus_counter()
        if self.snake_self_collision():
            self.game_is_over = True
            return
        if self.snake_board_collision():
            self.game_is_over = True
            return
        if self.snake_bomb_collision():
            self.game_is_over = True
            return
        self.eat_apples()
        if self.bomb.get_dead_status():
            self.bomb = self.create_bomb()
        self.bomb.singel_turn()
        self.bomb_outside_board()
        if self.snake_bomb_collision():
            self.game_is_over = True
            return
        self.bomb_apple_collision()

    def snake_self_collision(self):
        if len(set(self.snake.get_coordinates())) < len(
                self.snake.get_coordinates()):
            return True
        return False

    def snake_bomb_collision(self):
        for coord in self.bomb.get_coordinates():
            if coord in self.snake.get_coordinates():
                return True
        return False

    def check_eat_apple(self):
        for apple in self.apples:
            if apple.get_location() in self.snake.get_coordinates():
                return True

    def eat_apples(self):
        del_list = []
        for apple in self.apples:
            if apple.get_location() in self.snake.get_coordinates():
                del_list.append(apple)

        for apple in del_list:
            self.apples.remove(apple)
            self.score += apple.get_score()
            self.apples.append(self.create_apple())
            self.snake.eat_apple()

    def bomb_apple_collision(self):
        del_list = []
        for apple in self.apples:
            if apple.get_location() in self.bomb.get_coordinates():
                del_list.append(apple)

        for apple in del_list:
            self.apples.remove(apple)
            self.apples.append(self.create_apple())

    def bomb_outside_board(self):
        for sole_coord in self.bomb.get_coordinates():
            if sole_coord[0] >= gp.WIDTH or sole_coord[1] >= gp.HEIGHT:
                self.bomb = self.create_bomb()
                return
            if sole_coord[0] < 0 or sole_coord[1] < 0:
                self.bomb = self.create_bomb()
                return

    def snake_board_collision(self):
        for sole_coord in self.snake.get_coordinates():
            if sole_coord[0] >= gp.WIDTH or sole_coord[1] >= gp.HEIGHT:
                return True
            if sole_coord[0] < 0 or sole_coord[1] < 0:
                return True
        return False
