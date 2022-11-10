import pygame
import random

from random import choice
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager():

    def __init__(self):
        self.obstacles = []
        self.step = 0
        

    def update(self, game):
        
        if len(self.obstacles) == 0:
            random_obstacle = choice([choice([SMALL_CACTUS,LARGE_CACTUS]),BIRD])
               
            if random_obstacle ==  SMALL_CACTUS or random_obstacle == LARGE_CACTUS:
                obstacle = Cactus(random_obstacle) 
            if random_obstacle == LARGE_CACTUS:
                obstacle.rect.y = 295
            elif random_obstacle == BIRD:
                obstacle = Bird(random_obstacle)
                     
            self.obstacles.append(obstacle)
            

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.death_count += 1
                
                game.playing = False
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles = []
        