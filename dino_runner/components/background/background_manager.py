from random import randint
from dino_runner.utils.constants import CLOUD, SKY
from dino_runner.components.background.cloud import Cloud

class BakgroundManager():
    def __init__(self):
        self.items = []
        self.background_img = [CLOUD, SKY]
        self.type = 0
        
        

    def update(self,game,type): 
        if len(self.items) == 0:
            item = Cloud(self.background_img[type])
            self.items.append(item)

        for item in self.items :
            item.update(game.cloud_num,self.items)
        

    def draw(self,screen):
        x = 0
        for i in range(0,4):
            for item in self.items:
                item.draw(screen,x)
            x += 200

    def reset(self):
        self.items = []