import pygame

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.area = self.width * self.height

        # just use this I guess?
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def draw(self, screen):
        pass

    def update (self, dt):
        pass

    def collision_check(self, other_shape):
        pass
        