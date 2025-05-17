import pygame
from rectangle import Rectangle
from constants import *

class Ball(Rectangle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.velocity.x = 1
        self.velocity.y = 1

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect)

    def update(self, dt):
        self.move(dt)
        
    def move(self, dt):
        self.rect.x += self.velocity.x * BALL_SPEED * dt
        self.rect.y += self.velocity.y * BALL_SPEED * dt
