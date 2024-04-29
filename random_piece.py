import random
from game_pieces import *


def create_random_stone():
    shapes = [ZShape, SShape, IShape, OShape, JShape, LShape, TShape]
    random_shape = random.choice(shapes)
    return random_shape()
