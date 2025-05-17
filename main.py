# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from rectangle import Rectangle
from ball import Ball
from boundary import Boundary

def main():
    pygame.init()
    pygame.font.init()
    print("Starting Breakout!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = Ball(BALL_START_X, BALL_START_Y, BALL_WIDTH, BALL_HEIGHT)
    boundary_left = Boundary(BOUNDARY_LEFT_X, BOUNDARY_LEFT_Y, BOUNDARY_WIDTH, BOUNDARY_HEIGHT)
    boundary_right = Boundary(BOUNDARY_RIGHT_X, BOUNDARY_RIGHT_Y, BOUNDARY_WIDTH, BOUNDARY_HEIGHT)
    boundary_top = Boundary(BOUNDARY_TOP_X, BOUNDARY_TOP_Y, BOUNDARY_TOP_WIDTH, BOUNDARY_TOP_HEIGHT)

    clock = pygame.time.Clock()
    dt = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        player.draw(screen)
        ball.draw(screen)
        boundary_left.draw(screen)
        boundary_right.draw(screen)
        boundary_top.draw(screen)
        player.update(dt)
        ball.update(dt)
        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
