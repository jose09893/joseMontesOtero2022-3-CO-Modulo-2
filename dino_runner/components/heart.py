
from dino_runner.utils.constants import HEART

class Heart():
    def __init__(self):
        self.image = HEART
        self.image_rect = self.image.get_rect()
        self.image_rect.y = 20
        self.image_rect.x = 20
        
        
    def draw(self,screen,live):
        f = 0
        for i in range(0,live):
            screen.blit(self.image, (self.image_rect.x + f, self.image_rect.y))
            f += 30
