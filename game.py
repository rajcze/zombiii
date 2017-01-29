import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from player import player
import math


WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

def draw_player(player, X, Y):	
	#pygame.draw.line(window,(50,200,0),(X,Y),(X+(player.left_x*player.left_c),Y+(player.left_y*player.left_c)),1)
	#pygame.draw.line(window,(50,200,0),(X,Y),(X+(player.top_x*player.top_c),Y+(player.top_y*player.top_c)),1)
	#pygame.draw.line(window,(50,200,0),(X,Y), (X+(player.right_x*player.right_c),Y+(player.right_y*player.right_c)),1)
	pygame.draw.lines(window,(50,200,0), True, ((X+(player.left_x*player.left_c),Y+(player.left_y*player.left_c)), 
												(X+(player.top_x*player.top_c),Y+(player.top_y*player.top_c)),
												(X+(player.right_x*player.right_c),Y+(player.right_y*player.right_c))), 1)

if __name__ == "__main__":
	pygame.init()
	clock = pygame.time.Clock()
	window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
	player = player()
	player.rotate((45+180)*(math.pi/180))
	enemy = 0
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
		#pygame.draw.circle(window,(255,0,0),(800, 450), 30, 1)
		
		if left:
			player.all_rotate_left()
		if right:
			player.all_rotate_right()

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
		enemy += 1
		if enemy % 50 == 0:
			print(enemy)
		pygame.display.update()