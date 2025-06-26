from circleshape import *
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # set the instance properties
        super().__init__(x, y, radius)

    # override the draw method
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # override the update method
    def update(self, dt):
        self.position = (self.velocity * dt) + self.position

    def split(self):
        # the current asteroid will always disappear
        self.kill()
        # shot a small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # hit a non-small asteroid
        else:
            # generate a random angle between 20 to 50
            rand_num = random.uniform(20, 50)
            # use rotate on velocity to make two new vectors
            new_vel1 = self.velocity.rotate(rand_num)
            new_vel2= self.velocity.rotate(-rand_num)
            # radius of the new smaller asteriods
            self.radius = self.radius - ASTEROID_MIN_RADIUS
            # create two new asteroid objects
            new_ast1 = Asteroid(self.position[0], self.position[1], self.radius)
            new_ast2 = Asteroid(self.position[0], self.position[1], self.radius)
            # set their velocity
            new_ast1.velocity = new_vel1 * 1.2
            new_ast2.velocity = new_vel2 * 1.2
    