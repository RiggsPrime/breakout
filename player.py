import pygame
from rectangle import Rectangle
from constants import *

class Player(Rectangle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        
    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.rect.x > 0:
            self.move(-dt)
        if keys[pygame.K_d] and self.rect.x <= 1280 - PLAYER_WIDTH:
            self.move(dt)

    def move(self, dt):
        self.rect.x += PLAYER_SPEED * dt
        