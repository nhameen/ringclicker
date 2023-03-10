import pygame
import random
from settings import Settings

class Targets():
    
    def __init__(self):        
        self.settings = Settings()
        # Size for target img
        # TODO Make img change size according to time/score or randomize
        target_w = 50 # Width
        target_h = 50 # Height
        self.target_size = (target_w, target_h)

        # Set spawn delay
        self.spawn_delay = 1
        
        # Loads image
        self.image = pygame.transform.scale(pygame.image.load("assets/ring1.bmp"), self.target_size)
        self.rect = self.image.get_rect() 
        # Set random spawns       
        self.rect.x = random.randrange(50,1150) 
        self.rect.y = random.randrange(50,750)    
        
        # Target hitbox
        self.hitbox = (self.rect.x, self.rect.y, 50, 50 )
        # Target value 
        self.value = 1

        
            
    def spawn_target(self):
        t = Targets()
        return t
  