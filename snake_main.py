#################################################################
# FILE : apple.py
# WRITER 1 : noam shabat , no.amshabat1 , 206515579
# WRITER 2 : Eden Faingold, edenfaingold, 318227113
# EXERCISE : intro2cs2 ex10 2021
# DESCRIPTION: The main loop that runs the game
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: stackoverflow.com
#################################################################

from game import Game
from game_display import GameDisplay


def main_loop(gd: GameDisplay) -> None:
    game = Game()
    for x, y, color in game.get_colored_coordinates():
        gd.draw_cell(x, y, color)
    gd.show_score(game.get_score())
    gd.end_round()
    while True:
        key_clicked = gd.get_key_clicked()
        if key_clicked is None:
            key_clicked = game.get_snake_direction()
        game.single_turn(key_clicked)
        for x, y, color in game.get_colored_coordinates():
            gd.draw_cell(x, y, color)
        gd.show_score(game.get_score())
        gd.end_round()
        if game.is_over():
            break