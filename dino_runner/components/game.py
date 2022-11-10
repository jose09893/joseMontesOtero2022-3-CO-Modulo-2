import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE,COLORS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

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
        self.running = False
        self.score = 0
        self.hig_score = 0
        self.death_count = 0
        self.color_menu = COLORS["white"]

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def reset_all(self):
        self.obstacle_manager.reset_obstacle()
        self.player.dino_ducking = False
        self.game_speed = 20
        self.score = 0

    def run(self):
        self.reset_all()
        # Game loop: events - update - draw
        self.playing = True
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
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen) ## funcion draw de la clase dinosaur 
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def show_text(self,half_screen_width,half_screen_height,color):
        font = pygame.font.Font(None, 30)
        text = font.render("press any key to start ...", True, (color))
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text, text_rect) 

    def show_result(self,half_screen_width, half_screen_height,color):
        font = pygame.font.Font(None, 30)
        show_result = [font.render(f"Your Score: {self.score}", True, (color))
        ,font.render(f"Highest score: {self.hig_score}", True, (color)) 
        ,font.render(f"total deaths: {self.death_count}", True, (color))]
        i = 0
        for result in show_result:
                i += 30
                result_rect = result.get_rect()
                result_rect.center = (half_screen_width, half_screen_height)
                self.screen.blit(result, (result_rect.x, result_rect.y + i))

    def show_menu(self):
        self.screen.fill(self.color_menu)
        half_screen_height = SCREEN_HEIGHT // 2 ##para que sea entero
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.show_text(half_screen_width, half_screen_height, COLORS["black"])
        else:##pantalla de muerte
            self.show_text(half_screen_width, half_screen_height, COLORS["black"])
            self.show_result(half_screen_width, half_screen_height, COLORS["black"])
            
            

            

        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
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
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)
            
    def update_score(self):
        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5
        self.score += 1
        if self.hig_score < self.score:
                self.hig_score = self.score
    