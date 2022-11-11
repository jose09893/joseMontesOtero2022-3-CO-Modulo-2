
from dino_runner.components.background.item_background import ItemsBackground

from random import randint
class Cloud(ItemsBackground):
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect_width = self.rect.width
        self.x = randint(3,5)
        super().__init__(self.image,self.x)