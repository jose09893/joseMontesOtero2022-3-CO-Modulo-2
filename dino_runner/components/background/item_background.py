import pygame
from random import randint
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class ItemsBackground(Sprite):
    def __init__(self,image,x):
        self.speed = 8.5
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.x = x
        self.y = 175

        

    def update(self, cloud_num, items):
        self.rect.x -= (8)
        
        if (self.rect.x + 500 < -self.rect.width):##sale de pantalla
            items.pop()
            self.y = randint(140 ,175)

                

                
       

    def draw(self,screen,separator):
        screen.blit(self.image, (self.rect.x + separator, self.rect.y + self.y))
        