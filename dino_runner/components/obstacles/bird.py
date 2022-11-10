import random
from random import choice
from dino_runner.components.obstacles.obstacle import Obstacle
#from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    #BIRD_POS = [300,260,255,240 ]

    def __init__(self,image):
        super().__init__(image, 0)
        self.rect.y = random.randint(255, 300)
        
    

    
        
    



    
