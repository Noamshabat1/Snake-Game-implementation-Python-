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
