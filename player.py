from circleshape import *
from constants import *
from shot import Shots

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        foward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + foward * self.radius
        b = self.position - foward * self.radius - right
        c = self.position - foward * self.radius + right
        return [a, b, c]

    # override the draw method
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation = (PLAYER_TURN_SPEED * dt) + self.rotation

    def update(self, dt):
        # reduce the timer 
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # reverse dt 
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # check if they completed the 0.3 delay if so shoot again
        # if they haven't passed the timer check do nothing
        if not self.timer > 0:
            shot = Shots(self.position[0], self.position[1])
            self.timer = PLAYER_SHOOT_COOLDOWN
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

