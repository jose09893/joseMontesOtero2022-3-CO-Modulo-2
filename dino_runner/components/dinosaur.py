import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect() ## debuelve un rectangulo con la imagen
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.jump_speed = 8.5
        self.step_index = 0
        self.clock = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False


    def update(self, user_input): 
        if self.clock >= 2:
            if self.dino_run == True:
                self.run()
        
               
            elif self.dino_jump == True:
                self.jump()
            
            
            elif self.dino_duck == True:
                self.duck()
        
          
            

       
            if user_input[pygame.K_DOWN]  and not self.dino_duck:
                self.dino_duck = True
                self.dino_run = False
                self.clock = 0

        
        
         
            if user_input[pygame.K_UP]  and not self.dino_jump and not self.dino_duck :
                self.dino_jump = True
                self.dino_run = False
                self.dino_duck  = False
                self.clock = 0
            elif user_input[pygame.K_UP]  and  self.dino_duck :
                self.dino_duck = False
                self.dino_run = True
                self.clock = 0
            elif not self.dino_jump  and not self.dino_duck:
                self.dino_jump = False     
                self.dino_run = True
                self.dino_duck = False

            if self.step_index >= 10:
                self.step_index = 0 

        else:
            self.clock+=1

    def run(self):
        # cambio de imagen de dino 
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1 #contamos

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.5

        
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED


    def duck(self):
        
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = 340
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))