from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random 

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius,LINE_WIDTH)
    
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20,50)
            pos_new_vect =self.velocity.rotate(rand_angle)
            neg_new_vect =self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x,self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x,self.position.y, new_radius)
            asteroid_1.velocity = pos_new_vect * 1.2
            asteroid_2 = neg_new_vect * 1.2