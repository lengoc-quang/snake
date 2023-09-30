#Test
import pygame
import time
import random

apple = pygame.image.load("images\\apple.png")
buff = pygame.image.load("images\\buff.png")

pygame.init()
fonts = pygame.font.SysFont('segoe ui', 20, True)
text = fonts.render('Play game', True, (255,255,255))
easy = fonts.render('Easy', True, (255,0,0))
medium = fonts.render('Medium', True, (255,0,0))
hard = fonts.render('Hard', True, (255,0,0))
window_x = 800      
window_y = 600 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255,0)
blue = pygame.Color(0, 0, 255)
orange = pygame.Color(255, 128, 64)
yellow = pygame.Color(255,255,0)
width = 220
height = 270
color_light = (230,240,28)
color_dark = (204,214,14)
score=0
bonus = 0
score = 0
speed_choose= False

game_state = "Start"
start_background=pygame.image.load('images//start.png')

pygame.display.set_caption(' Pygame Snakes')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

#bg
bg = pygame.image.load("images\\bg.jpg")
pygame.mixer.Channel(0).set_volume(0.1)
pygame.mixer.Channel(0).play(pygame.mixer.Sound('media\\bg.mp3'), -1)


def show_score(choice, color, font, size):
	score_font = pygame.font.SysFont(font, size, True)
	score_surface = score_font.render('Score : ' + str(score), True, color)
	score_rect = score_surface.get_rect()
	game_window.blit(score_surface, score_rect)

def game_over():
	my_font = pygame.font.SysFont('segoe ui', 50)
	game_over_surface = my_font.render('Your score is : ' + str(score), True, red)
	game_over_rect = game_over_surface.get_rect()
	game_over_rect.midtop = (window_x/2, window_y/4)
	game_window.blit(game_over_surface, game_over_rect)
	pygame.mixer.music.stop()
	pygame.display.flip()
	time.sleep(3)
	pygame.quit()
	quit()

def eat():
	global bonus,score
	pygame.mixer.Channel(1).set_volume(0.5)
	pygame.mixer.Channel(1).play(pygame.mixer.Sound('media\\pop.mp3'))
	if bonus == 5:
		score += 10
		bonus = 0
	else:
		score +=1
		bonus += 1

def speeds():
	global speed,game_state,speed_choose
	game_window.blit(start_background, (0,0))
	game_window.blit(easy, (width+25,height+10))
	game_window.blit(medium , (width+105,height+10))
	game_window.blit(hard , (width+220,height+10))
	for event in pygame.event.get():
		mouse_ps = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if width <= mouse_ps[0] <= width+90 and height <= mouse_ps[1] <= height+40:
				speed=10
				game_state="Games"
				time.sleep(0.2)
				games()
				break
			elif width+100 <= mouse_ps[0] <= width+190 and height <= mouse_ps[1] <= height+40:
				speed=15
				game_state="Games"
				time.sleep(0.2)
				games()
				break
			elif width+200 <= mouse_ps[0] <= width+290 and height <= mouse_ps[1] <= height+40:
				speed=25
				game_state="Games"
				time.sleep(0.2)
				games()
				break
		if event.type == pygame.QUIT:
			pygame.display.quit()
			pygame.quit()
			quit()

def games():
	global bonus,score
	snake_position = [100, 50] 
	snake_body = [ [100, 50],
					[90, 50],
					[80, 50],
					[70, 50]
				]
	fruit_position = [random.randint(4, 78)*10,
					random.randint(4, 58)*10]
	fruit_spawn = True
	direction = 4
	change_to=4
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					change_to = 1
				if event.key == pygame.K_DOWN:
					change_to = 2
				if event.key == pygame.K_LEFT:
					change_to = 3
				if event.key == pygame.K_RIGHT:
					change_to = 4
		if change_to == 1 and direction != 2:
			direction = 1
		if change_to == 2 and direction != 1:
			direction = 2
		if change_to == 3 and direction != 4:
			direction = 3
		if change_to == 4 and direction != 3:
			direction = 4
		if direction == 1:
			snake_position[1] -= 10
		if direction == 2:
			snake_position[1] += 10
		if direction == 3:
			snake_position[0] -= 10
		if direction == 4:
			snake_position[0] += 10
		snake_body.insert(0, list(snake_position))
		if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
			eat()
			fruit_spawn = False
		else:
			snake_body.pop()
		if not fruit_spawn:
			fruit_position = [random.randrange(1, (window_x//10)) * 10,
							random.randrange(1, (window_y//10)) * 10]
			fruit_spawn = True
		game_window.blit(bg, (0,0))
	# vẽ rắn
		for pos in snake_body:
			pygame.draw.rect(game_window, white, pygame.Rect(
			pos[0], pos[1], 10, 10))
	# vẽ táo
		if bonus!=5:
			game_window.blit(apple, (fruit_position[0],fruit_position[1]))
		else:
			game_window.blit(buff, (fruit_position[0],fruit_position[1]))
	# vẽ tường
		wall = pygame.image.load("images\\wall.png")
		game_window.blit(wall, (0,0))
		if snake_position[0] < 20 or snake_position[0] > window_x-30:
			game_over()
		if snake_position[1] < 20 or snake_position[1] > window_y-30:
			game_over()
		for block in snake_body[1:]:
			if snake_position[0] == block[0] and snake_position[1] == block[1]:
				game_over()
		show_score(1, white, 'segoe ui', 20)
		pygame.display.update()
		fps.tick(speed)

speed=0        
game_window.blit(start_background, (0,0))

def choose():
	while game_state!="Game":
		if speed_choose==True:
			speeds()
		pygame.display.update()

while game_state=="Start":
	for event in pygame.event.get():
		mouse = pygame.mouse.get_pos()
		if width <= mouse[0] <= width+300 and height <= mouse[1] <= height+40:
			pygame.draw.rect(game_window,color_dark,[width,height,300,40])
		else:
			pygame.draw.rect(game_window,color_light,[width,height,300,40])
		game_window.blit(text , (width+100,height+10))
		if event.type == pygame.MOUSEBUTTONDOWN:
			if width <= mouse[0] <= width+300 and height <= mouse[1] <= height+40:
				speed_choose=True
				choose()
				break
		if event.type == pygame.QUIT:
			pygame.display.quit()
			pygame.quit()
			quit()
	pygame.display.update()