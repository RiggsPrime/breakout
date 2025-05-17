import pygame
from rectangle import Rectangle
from constants import *

class Boundary(Rectangle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect)
