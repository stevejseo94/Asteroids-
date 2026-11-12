import pygame
import random 
from constants import LINE_WIDTH , ASTEROID_MIN_RADIUS 
from circleshape import CircleShape 
from logger import log_event

class Asteroid(CircleShape): 
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius) 
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt): 
        self.position += self.velocity * dt 
    
    def split(self): 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return 
        else: 
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50) 
            old_radius = self.radius 
            new_radius = old_radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius) 
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius) 

            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2 
        


    