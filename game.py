import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
from player import player
import enemy

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
def draw_bullet(bullet, X, Y):
    pygame.draw.line(window, bullet.color, (bullet.x, bullet.y), (X + bullet.x_speed, Y + bullet.y_speed), 1)

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    player = player()
    player.rotate((45+180)*(math.pi/180))
    enemies = []
    level = 1
    intervals = [40]
    difficulty = 80
    lastEnemyCreated = 0
    gameStarted = False
    '''
    print(player.get_deg_rotation())
    print("X: ", player.get_x())
    print("Y: ", player.get_y())
    '''
    left = False
    right = False
    shoot = False
    while True:
        '''
        print(player.get_deg_rotation())
        print("X: ", player.get_x())
        print("Y: ", player.get_y())
        '''
        window.fill((0,0,0))
        
        draw_player(player, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        for bullet in player.bullets:
            draw_bullet(bullet, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        #pygame.draw.circle(window,(255,0,0),(800, 450), 30, 1)


        if GAME_TIME.get_ticks() - lastEnemyCreated > intervals[level-1] and gameStarted is True:
            enemyShips.append(ships.Enemy(random.randint(0, windowWidth), -60, pygame, surface, 1))
            lastEnemyCreated = GAME_TIME.get_ticks()
        
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
                if event.key == pygame.K_SPACE:
                    player.shoot(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False

        clock.tick(60)

        pygame.display.update()