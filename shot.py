from circleshape import *
from constants import SHOT_RADIUS

class Shots(CircleShape):
    def __init__(self, x, y):
        # set the instance properties
        super().__init__(x, y, SHOT_RADIUS)

    # override the draw method
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # override the update method
    def update(self, dt):
        self.position = (self.velocity * dt) + self.position