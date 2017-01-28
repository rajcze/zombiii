import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from player import player
import math


WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

def draw_player(player, X, Y):
	x_pos = -50*player.x
	y_pos = -50*player.y
	num = 70/math.sqrt((x_pos*x_pos)+(y_pos*y_pos))
	print(num)
	print(math.sqrt((x_pos*x_pos*num)+(y_pos*y_pos*num)))
	pygame.draw.line(window,(50,200,0),(X,Y),((X+x_pos)*num,(Y+y_pos)*num),10)
	#pygame.draw.lines(window,(50,200,0), True, ((WINDOW_WIDTH/2+(20*player.x), 450+(40*player.y)), (WINDOW_WIDTH/2+(-50*player.x),WINDOW_HEIGHT/2+(-50*player.y)), (800+(-20*player.x), 450+(40*player.y))), 1)

if __name__ == "__main__":
	pygame.init()
	clock = pygame.time.Clock()
	window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
	player = player()
	left = False
	right = False
	while True:
		window.fill((0,0,0))
		draw_player(player, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

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