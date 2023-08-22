import pygame as pg
from constans import SQUARE_WIDTH, SQUARE_HEIGHT


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.eat = pg.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HEIGHT)

    def draw(self, screen):
        pg.draw.rect(screen, "red", self.eat)
