import pygame
import random
from random import choice
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import  BIRD

class Obstacle(Sprite):
    
    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0
        

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        
        self.fly()

        if self.step_index >= 10:
                self.step_index = 0 

        if self.rect.x < -self.rect.width:##sale de pantalla
            obstacles.pop()
            

    def fly(self):
        if self.image == BIRD:
            self.obstacle_type = 0 if self.step_index < 5 else 1
            self.step_index += 1
            
        else:
            pass
            


    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type],(self.rect.x, self.rect.y))