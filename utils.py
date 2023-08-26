import random

from constants import SQUARE_WIDTH,SQUARE_HEIGHT,NUM_X,NUM_Y


def generate_position(num_x=NUM_X, num_y=NUM_Y):
    x, y = random.choice(range(num_x)) * SQUARE_WIDTH, random.choice(range(num_y)) * SQUARE_HEIGHT
    return x, y

