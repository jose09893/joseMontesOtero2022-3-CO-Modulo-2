import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE,COLORS,GAME_OVER_TEXT,DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.Power_Ups.power_up_manager import PowerUpManager
from dino_runner.components.message import draw_message

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
        self.running = False
        self.score = 0
        self.hig_score = 0
        self.death_count = 0
        self.color_menu = COLORS["white"]
        self.text_color = 'black'
        self.text_score_color = 'blue'

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def reset_all(self):
        self.text_score_color = 'blue'
        self.power_up_manager.reset_power_ups()
        self.obstacle_manager.reset_obstacle()
        self.player.dino_ducking = False
        self.game_speed = 20
        self.score = 0
        self.playing = True

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
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed() ## obtener tecla
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen) ## funcion draw de la clase dinosaur 
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()
    
    

    # def show_text(self,half_screen_width,half_screen_height,color):
     #   font = pygame.font.Font(None, 30)
      #  text = font.render("press any key to start ...", True, (color))
       # text_rect = text.get_rect()
        #text_rect.center = (half_screen_width, half_screen_height)
        #self.screen.blit(text, text_rect) 

    # def show_result(self,half_screen_width, half_screen_height,color):
     #   font = pygame.font.Font(None, 30)
      #  show_result = [font.render(f"Your Score: {self.score}", True, (COLORS[color]))
       # ,font.render(f"Highest score: {self.hig_score}", True, (COLORS[color])) 
        #,font.render(f"total deaths: {self.death_count}", True, (COLORS[color]))]
        #i = 0
        #for result in show_result:
         #       i += 30
          #      result_rect = result.get_rect()
           #     result_rect.center = (half_screen_width, half_screen_height)
            #    self.screen.blit(result, (result_rect.x, result_rect.y + i))

    def show_menu(self):
        self.screen.fill(self.color_menu)
        half_screen_height = SCREEN_HEIGHT // 2 ##para que sea entero
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message("press any key to start ...", self.screen)
            #self.show_text(half_screen_width, half_screen_height, self.text_color)
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        else:##pantalla de muerte
            draw_message("press any key to restart ...", self.screen)
            draw_message(f"Your Score: {self.score}",self.screen,pos_y_center = half_screen_height + 30)
            draw_message(f"Highest score: {self.hig_score}",self.screen,pos_y_center = half_screen_height + 60)
            draw_message(f"total deaths: {self.death_count}",self.screen,pos_y_center = half_screen_height + 90)
            GAME_OVER_TEXT_RECT = GAME_OVER_TEXT.get_rect()
            GAME_OVER_TEXT_RECT.center = (half_screen_width, half_screen_height)
            self.screen.blit(GAME_OVER_TEXT, (GAME_OVER_TEXT_RECT.x, GAME_OVER_TEXT_RECT.y - 100))
            #self.show_text(half_screen_width, half_screen_height, self.text_color)
            #self.show_result(half_screen_width, half_screen_height, self.text_color)    

        
        pygame.display.update()
        self.handle_event_on_menu()




    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
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
        if self.score > 500 :
            self.text_score_color = "red"
    