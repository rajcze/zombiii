import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from player import player
import math


WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

def draw_player(player, X, Y):
	top_x = -40*player.x
	top_y = -40*player.y
	top_c = 70/math.sqrt((top_x*top_x)+(top_y*top_y))
	left_x = 10*player.x
	left_y = 40*player.y
	left_c = 50/math.sqrt((left_x*left_x)+(left_y*left_y))
	right_x = 40*player.x
	right_y = 10*player.y
	right_c = 50/math.sqrt((right_x*right_x)+(right_y*right_y))
	
	#pygame.draw.line(window,(50,200,0),(X,Y),(X+(left_x*left_c),Y+(left_y*left_c)),1)
	#pygame.draw.line(window,(50,200,0),(X,Y),(X+(top_x*top_c),Y+(top_y*top_c)),1)
	#pygame.draw.line(window,(50,200,0),(X,Y), (X+(right_x*right_c),Y+(right_y*right_c)),1)
	pygame.draw.lines(window,(50,200,0), True, ((X+(left_x*left_c),Y+(left_y*left_c)), (X+(top_x*top_c),Y+(top_y*top_c)) , (X+(right_x*right_c),Y+(right_y*right_c))), 1)

if __name__ == "__main__":
	pygame.init()
	clock = pygame.time.Clock()
	window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
	player = player()
	#player.rotate((45)*(math.pi/180))
	'''
	print(player.get_deg_rotation())
	print("X: ", player.get_x())
	print("Y: ", player.get_y())
	'''
	left = False
	right = False
	while True:
		'''
		print(player.get_deg_rotation())
		print("X: ", player.get_x())
		print("Y: ", player.get_y())
		'''
		window.fill((0,0,0))
		
		draw_player(player, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
		pygame.draw.circle(window,(255,0,0),(800, 450), 70, 1)
		
		if left:
			player.rotate_left()
		if right:
			player.rotate_right()

		for event in GAME_EVENTS.get():
			if event.type == GAME_GLOBALS.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					left = True
				if event.key == pygame.K_RIGHT:
					right = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					left = False
				if event.key == pygame.K_RIGHT:
					right = False
				
		clock.tick(60)
		pygame.display.update()