import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD,DEFAULT_TYPE,SHIELD_TYPE

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
JUM_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS_DUCKING = 345
    Y_POS = 310
    WIDTH_DINO_RUN = 65
    WIDTH_DINO_DUCKING = 100
    JUMP_SPEED = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        # self.image = RUNNING[0]
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect() #** debuelve un rectangulo con la imagen
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_rect.w = self.WIDTH_DINO_RUN
        self.jump_speed = 8.5
        self.step_index = 0
        self.clock = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_ducking = False
        self.has_power_up = False #? ¿el dino tiene poweerups?
        self.power_time_up = 0 



    def update(self, user_input): 
        
        if self.clock >= 2: #para que no se tome dos veces la tecla
            if self.dino_run == True:
                self.run()  
            elif self.dino_jump == True:
                self.jump()  
            elif self.dino_ducking == True:
                self.ducking()
       
            if user_input[pygame.K_DOWN]  and not self.dino_ducking and not self.dino_jump:
                self.dino_ducking = True
                self.dino_run = False
                self.clock = 0
         
            if user_input[pygame.K_UP]  and not self.dino_jump and not self.dino_ducking :
                self.dino_jump = True
                self.dino_run = False
                self.dino_ducking  = False
                self.clock = 0
            elif user_input[pygame.K_UP]  and  self.dino_ducking :
                self.dino_ducking = False
                self.dino_run = True
                self.clock = 0
            elif not self.dino_jump  and not self.dino_ducking:
                self.dino_jump = False     
                self.dino_run = True
                self.dino_ducking = False

            if self.step_index >= 9:
                self.step_index = 0 
        else:
            self.clock+=1

    def run(self):
        # cambio de imagen de dino 
        #self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_rect.w = self.WIDTH_DINO_RUN
        self.step_index += 1 #contamos

    def jump(self):
        self.image = JUM_IMG[self.type]
        self.dino_rect.y -= self.jump_speed * 3
        self.jump_speed -= 0.7

        
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED


    def ducking(self):
        
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCKING
        self.dino_rect.w = self.WIDTH_DINO_DUCKING
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))