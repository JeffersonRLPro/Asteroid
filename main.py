import pygame
from constants import *


def main():
    # initialize the pygame package
    pygame.init()
    print("Starting Asteroids!")
    # make the display 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create infinate loop
    while(True):
        # if the x is selected, quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill the screen with black
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
