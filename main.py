import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shots

def main():
    # initialize the pygame package
    pygame.init()
    print("Starting Asteroids!")
    # make the display 
    # create all game groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    # set the groups as containers of the Player and Asteroid object
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shots.containers = (shots, updatable, drawable)
    player = Player(x, y)
    asteroid_field = AsteroidField()

    # create varibales for FPS
    fps = pygame.time.Clock()
    dt = 1
    # create an infinate loop
    while(True):
        # if the x is selected, quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # pause the game for a bit to get 60 FPS
        dt = fps.tick(60) / 1000
        # fill the screen with black
        screen.fill("black")
        updatable.update(dt)
        # check if there were collisions with any astroid
        for asteroid in asteroids:
            # check if the player collided
            if asteroid.collision(player):
                print("Game over!")
                sys.exit(0)
            # check if the bullet collided
            for shot in shots:
                if asteroid.collision(shot):
                    # remove them
                    shot.kill()
                    asteroid.split()
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
