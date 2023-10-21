#Test
from game import *
speed=0        
game_window.blit(start_background, (0,0))
#choose speed
def choose():
	while game_state!="Games":
		if speed_choose==True:
			speeds_2()
		pygame.display.update()
#start menu
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
