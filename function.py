import pygame
import time

pygame.init()

direction = 4
change_to=4
h1 = pygame.image.load("images\\h1.png")
h2 = pygame.image.load("images\\h2.png")
h3 = pygame.image.load("images\\h3.png")
h4 = pygame.image.load("images\\h4.png")
body = pygame.image.load("images\\body.png")
apple = pygame.image.load("images\\apple.png")
buff = pygame.image.load("images\\buff.png")
wall = pygame.image.load("images\\wall.png")
wall2 = pygame.image.load("images\\obstruction.png")
wall3 = pygame.image.load("images\\obstruction.png")
fonts = pygame.font.SysFont('segoe ui', 20, True)
text = fonts.render('Play game', True, (255,255,255))
easy = fonts.render('Easy', True, (0,170,240))
medium = fonts.render('Medium', True, (0,170,240))
hard = fonts.render('Hard', True, (0,170,240))
window_x = 800      
window_y = 600 
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
width = 220
height = 270
color_light = (230,240,28)
color_dark = (204,214,14)
bonus = 0
score = 0
speed_choose = False
game_window = pygame.display.set_mode((window_x, window_y))
snake = pygame.draw.rect(game_window, white, pygame.Rect(
			100,50, 10, 10))
surf = pygame.Surface((snake.w, snake.h))
game_state = "Start"
start_background=pygame.image.load('images//start.png')
pygame.display.set_caption(' Pygame Snakes')
fps = pygame.time.Clock()

#bg
bg = pygame.image.load("images\\bg.jpg")
pygame.mixer.Channel(0).set_volume(0.1)
pygame.mixer.Channel(0).play(pygame.mixer.Sound('media\\bg.mp3'), -1)

head_position = [100, 50]

def draw_snake_head():
	if direction == 1:
		game_window.blit(h1,head_position)
	if direction == 2:
		game_window.blit(h2,head_position)
	if direction == 3:
		game_window.blit(h3,head_position)
	if direction == 4:
		game_window.blit(h4,head_position)

#collision
def collision(surface1, pos1, surface2, pos2):
    mask1 = pygame.mask.from_surface(surface1)
    mask2 = pygame.mask.from_surface(surface2)
    x = pos2[0] - pos1[0]
    y = pos2[1] - pos1[1]
    if mask1.overlap(mask2, (x, y)) != None:
        return True
    return False
#show score
def show_score(choice, color, font, size):
	score_font = pygame.font.SysFont(font, size, True)
	score_surface = score_font.render('Score : ' + str(score), True, color)
	score_rect = score_surface.get_rect()
	game_window.blit(score_surface, score_rect)
#game over
def game_over():
	my_font = pygame.font.SysFont('segoe ui', 50)
	game_over_surface = my_font.render('Your score is : ' + str(score), True, red)
	game_over_rect = game_over_surface.get_rect()
	game_over_rect.midtop = (400,250) #type: ignore
	game_window.blit(game_over_surface, game_over_rect)
	pygame.mixer.music.stop()
	pygame.display.flip()
	time.sleep(3)
	pygame.quit()
	quit()
#eating
def eat():
	global bonus,score
	pygame.mixer.Channel(1).set_volume(0.5)
	pygame.mixer.Channel(1).play(pygame.mixer.Sound('media\\pop.mp3'))
	if bonus != 5:
		score += 1
		bonus += 1
	else:
		score += 1
		bonus = 0
