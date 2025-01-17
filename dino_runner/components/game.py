import pygame
from random import randint
from dino_runner.utils.constants import BG,SKY, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE,COLORS,GAME_OVER_TEXT,DEFAULT_TYPE,HEART
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.background.background_manager import BakgroundManager
from dino_runner.components.heart import Heart
from dino_runner.components.message import draw_message
from dino_runner.components.save_score import save_score, show_score


class Game:
    
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.background_manager = BakgroundManager()
        self.hearts_manager = Heart()
        self.running = False
        self.score = 0
        self.hig_score = 0
        self.death_count = 0
        self.hearts = 3
        self.color_menu = COLORS["white"]
        self.background_color = COLORS["white"]
        self.text_color = 'black'
        self.text_score_color = 'blue'
        self.cloud_num = randint(3 , 5)
        self.type_img_background = 0
        self.background_img = BG
        self.night_duration = 6
        self.day = True
        self.score_night = 500
        self.user_name = "jose"
        self.arch = open("score.txt", "a")
        self.text_r = open("score.txt", "r")
        

    def execute(self):
        #self.user_name = input("name")
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        save_score(self)
        pygame.quit()

    def reset_all(self):
        self.hearts = 3
        self.text_score_color = "blue"
        self.background_color = COLORS["white"]
        self.background_img = BG
        self.y_pos_bg = 380
        self.score_night = 500
        self.text_score_color = 'blue'
        self.power_up_manager.reset_power_ups()
        self.obstacle_manager.reset_obstacle()
        self.background_manager.reset()
        self.player.dino_ducking = False
        self.game_speed = 20
        self.score = 0
        self.playing = True
        self.day = True

    def run(self):
        self.reset_all()
        
        # Game loop: events - update - draw
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.arch.close()
                self.playing = False
                

    def update(self):
        user_input = pygame.key.get_pressed() ## obtener tecla
        self.background_manager.update(self,self.type_img_background)
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        
        
        #for i in range(self.cloud_num):
            #self.background_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(self.background_color)
        self.background_manager.draw(self.screen)
        self.draw_background()
        self.player.draw(self.screen) ## funcion draw de la clase dinosaur 
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        
        #x = 0
        #for i in range(self.cloud_num):
        #    self.background_manager.draw(self.screen,x)
        #    x += 200
        
        self.night()
        self.draw_power_up_time()
        self.draw_score()
        self.hearts_manager.draw(self.screen,self.hearts)
        
        pygame.display.update()
        pygame.display.flip()
    

    def show_menu(self):
        
        self.screen.fill(self.color_menu)
        half_screen_height = SCREEN_HEIGHT // 2 ##para que sea entero
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message("press any key to start ...", self.screen)
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        else:##pantalla de muerte
            #draw_message("press any key to restart ...", self.screen)
            #draw_message(f"Your Score: {self.score}",self.screen,pos_y_center = half_screen_height + 30)
            #draw_message(f"Highest score: {self.hig_score}",self.screen,pos_y_center = half_screen_height + 60)
            #draw_message(f"total deaths: {self.death_count}",self.screen,pos_y_center = half_screen_height + 90)
            GAME_OVER_TEXT_RECT = GAME_OVER_TEXT.get_rect()
            GAME_OVER_TEXT_RECT.center = (half_screen_width, half_screen_height)
            self.screen.blit(GAME_OVER_TEXT, (GAME_OVER_TEXT_RECT.x, GAME_OVER_TEXT_RECT.y - 100))
            show_score(self,self.text_r)

           

        
        pygame.display.update()
        self.handle_event_on_menu()




    def draw_background(self):
        image_width = self.background_img.get_width()
        self.screen.blit(self.background_img, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(self.background_img, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width + 700:
            self.screen.blit(self.background_img, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def handle_event_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
    
    def draw_score(self):
        font = pygame.font.Font(None, 30)
        text = font.render(f"Score: {self.score}", True, (self.text_score_color))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >= 0:
                draw_message(f'{self.player.type} enable for {time_to_show} seconds', self.screen, font_color = "violet", font_size=18,pos_x_center=508,pos_y_center=50)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE


            
    def update_score(self):
        if self.score % 300 == 0 and self.game_speed < 500:
            self.game_speed += 5
        self.score += 1
        if self.hig_score < self.score:
                self.hig_score = self.score
        
        
            
    def night(self):
        
        if (self.score == self.score_night) and self.day == True:
                self.day = False 
                self.text_score_color = "red"
                self.background_color = COLORS["black"]
                self.background_img = SKY
                self.y_pos_bg = 0
                
        elif (self.score == self.score_night + 500) and self.day == False:
                self.day = True
                self.text_score_color = "blue"
                self.background_color = COLORS["white"]
                self.background_img = BG
                self.y_pos_bg = 380
                self.score_night= self.score_night + 1000   