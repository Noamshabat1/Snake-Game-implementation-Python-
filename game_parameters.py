#################################################################
# FILE : calculate_mathematical_expression
# WRITER : noam shabat , no.amshabat1 , 206515579
# WRITER : %%%%%% , %%%%%%%% , %%%%%%%%%%
# EXERCISE : intro2cs2 ex10 2021
# DESCRIPTION: A simple search engine that crawl's the web.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: stackoverflow.com
# NOTES: ...
#################################################################
import random
from typing import Tuple

WIDTH = 40
HEIGHT = 30


def get_random_apple_data() -> Tuple[int, int, int]:
    """
    This method returns randomly drawn data for the apple
    :return: (x,y,score) - Random location on the board and initial score
    """
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    score = random.randint(1, 5)

    return x, y, score


def get_random_bomb_data() -> Tuple[int, int, int, int]:
    """
    This method returns randomly drawn data for the bomb
    :return: (x,y,radius,time) Random location, bomb radius and time to explode
    """
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    radius = random.randint(2, 5)
    time = random.randint(20, 30)

    return x, y, radius, time
