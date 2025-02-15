from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

ASTEROID_COLORS = ["green", "blue", "white"]

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = ASTEROID_COLORS[self.radius // ASTEROID_MIN_RADIUS - 1]

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20,50)

            vector1 = self.velocity.rotate(random_angle) * 1.2
            vector2 = self.velocity.rotate(random_angle * -1) * 1.2
            
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = vector1 
            
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2.velocity = vector2

