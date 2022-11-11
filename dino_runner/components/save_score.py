from dino_runner.components.message import draw_message
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


scores = []
dicscores = {}
half_screen_height = SCREEN_HEIGHT // 2 ##para que sea entero
half_screen_width = SCREEN_WIDTH // 2

def save_score(game):
    game.arch.write(str(game.user_name) + "\n")
    game.arch.write(str(game.hig_score) + "\n")

def show_score(game,text):
    x = 70
    max = game.hig_score
    #draw_message(f"best scores:",game.screen,pos_y_center = 50 , pos_x_center =  200 )
    for letter in game.text_r:
        if "\n" in letter:
            letter = letter.replace("\n", "")
            scores.append(letter)
    for k in range(1,len(scores),2):
        if int(scores[k]) > max:
            max = int(scores[k])
    
    
    if max == game.hig_score:
        draw_message("press any key to restart ...", game.screen)
        draw_message(f"Your Score: {game.score}",game.screen,pos_y_center = half_screen_height + 30)
        draw_message(f"Highest score: {game.hig_score}",game.screen,pos_y_center = half_screen_height + 60)
        draw_message(f" new best score: {max} ",game.screen,pos_y_center = half_screen_height + 90)
        draw_message(f"total deaths: {game.death_count}",game.screen,pos_y_center = half_screen_height + 130)
        
    else:
        draw_message("press any key to restart ...", game.screen)
        draw_message(f"Your Score: {game.score}",game.screen,pos_y_center = half_screen_height + 30)
        draw_message(f"Highest score: {game.hig_score}",game.screen,pos_y_center = half_screen_height + 60)
        draw_message(f" {game.user_name} Your max Score: {max} ",game.screen,pos_y_center = half_screen_height + 90)
        draw_message(f"total deaths: {game.death_count}",game.screen,pos_y_center = half_screen_height + 130)
       
    #*for i in range(0,len(scores),2):
     #*   x += 70
      #*  users = scores[i]
       #* socre_user = scores[i+1] 
        #*draw_message(f" {users} Your Score: {socre_user} ",game.screen,pos_y_center =  x, pos_x_center =  200)

    
   
    
    

