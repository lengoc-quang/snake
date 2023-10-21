from function import *
import random
change_to=4
snake_position = [100, 50] 
snake_body = [	[90, 50],
				[80, 50],
				[70, 50]
			]
fruit_position = [random.randint(5, 75)*10,
				random.randint(5, 55)*10]
fruit_spawn = True
direction = 4
def menu_choose():
	game_window.blit(start_background, (0,0))
	game_window.blit(easy, (width+25,height+10))
	game_window.blit(medium , (width+105,height+10))
	game_window.blit(hard , (width+220,height+10))
def speeds():
	global speed,game_state,speed_choose
	menu_choose()
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
def speeds_2():
	global speed,game_state,speed_choose
	menu_choose()
	for event in pygame.event.get():
		mouse_ps = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if width <= mouse_ps[0] <= width+90 and height <= mouse_ps[1] <= height+40:
				speed=10
				game_state="Games"
				time.sleep(0.2)
				games_lv2()
				break
			elif width+100 <= mouse_ps[0] <= width+190 and height <= mouse_ps[1] <= height+40:
				speed=15
				game_state="Games"
				time.sleep(0.2)
				games_lv2()
				break
			elif width+200 <= mouse_ps[0] <= width+290 and height <= mouse_ps[1] <= height+40:
				speed=25
				game_state="Games"
				time.sleep(0.2)
				games_lv2()
				break
		if event.type == pygame.QUIT:
			pygame.display.quit()
			pygame.quit()
			quit()
def kb_input():
	global change_to,direction,head_position,fruit_position,fruit_spawn
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
		head_position[1] -=10
	if direction == 2:
		snake_position[1] += 10
		head_position[1] += 10
	if direction == 3:
		snake_position[0] -= 10
		head_position[0] -= 10
	if direction == 4:
		snake_position[0] += 10
		head_position[0] += 10
	snake_body.insert(0, list(snake_position))
	if collision(h1, head_position, apple, fruit_position)==True or collision(h1, head_position, buff, fruit_position):
		eat()
		fruit_spawn = False
	elif collision(h2, head_position, apple, fruit_position)==True or collision(h2, head_position, buff, fruit_position):
		eat()
		fruit_spawn = False
	elif collision(h3, head_position, apple, fruit_position)==True or collision(h3, head_position, buff, fruit_position):
		eat()
		fruit_spawn = False
	elif collision(h4, head_position, apple, fruit_position)==True or collision(h4, head_position, buff, fruit_position):
		eat()
		fruit_spawn = False
	else:
		snake_body.pop()
	if collision(wall2,(210,145),apple ,fruit_position)==True or collision(wall3,(210,390),apple ,fruit_position )==True:
		fruit_spawn = False
	if not fruit_spawn:
		fruit_position = [random.randint(5, 75)*10,
						random.randint(5, 55)*10]
		fruit_spawn = True
def games():
	global bonus,score,surf
	while True:
		kb_input()
		game_window.blit(bg, (0,0))
	# vẽ rắn
		for pos in snake_body:
			game_window.blit(body, (pos[0],pos[1]))
		draw_snake_head()
	# vẽ táo
		if bonus!=5:
			game_window.blit(apple, (fruit_position[0],fruit_position[1]))
		else:
			game_window.blit(buff, (fruit_position[0],fruit_position[1]))
	# vẽ tường
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
def games_lv2():
	global bonus,score,surf
	while True:
		kb_input()
		game_window.blit(bg, (0,0))
	# vẽ rắn
		for pos in snake_body:
			game_window.blit(body, (pos[0],pos[1]))
		draw_snake_head()
	# vẽ táo
		if bonus!=5:
			game_window.blit(apple, (fruit_position[0],fruit_position[1]))
		else:
			game_window.blit(buff, (fruit_position[0],fruit_position[1]))
	# vẽ vật cản
		game_window.blit(wall2, (210,145))
		game_window.blit(wall3, (210,390))
		if collision(h1, snake_position, wall2, (210,145))==True or collision(h1, snake_position, wall3, (210,390))==True:
			game_over()
		elif collision(h2, snake_position, wall2, (210,145))==True or collision(h2, snake_position, wall3, (210,390))==True:
			game_over()
		elif collision(h3, snake_position, wall2, (210,145))==True or collision(h3, snake_position, wall3, (210,390))==True:
			game_over()
		elif collision(h4, snake_position, wall2, (210,145))==True or collision(h4, snake_position, wall3, (210,390))==True:
			game_over()
	# vẽ tường
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
