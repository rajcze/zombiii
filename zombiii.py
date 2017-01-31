import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
from player import player
import enemy
import game
import math


def draw_player(player, X, Y):  
    #pygame.draw.line(window,(50,200,0),(X,Y),(X+(player.left_x*player.left_c),Y+(player.left_y*player.left_c)),1)
    #pygame.draw.line(window,(50,200,0),(X,Y),(X+(player.top_x*player.top_c),Y+(player.top_y*player.top_c)),1)
    #pygame.draw.line(window,(50,200,0),(X,Y), (X+(player.right_x*player.right_c),Y+(player.right_y*player.right_c)),1)
    pygame.draw.lines(window,player.color, True, ((X+(player.left_x*player.left_c),Y+(player.left_y*player.left_c)), 
                                                (X+(player.top_x*player.top_c),Y+(player.top_y*player.top_c)),
                                                (X+(player.right_x*player.right_c),Y+(player.right_y*player.right_c))), 2)

def draw_bullet(bullet, X, Y):
    pygame.draw.line(window, bullet.color, (bullet.x, bullet.y), (X + bullet.x_end, Y + bullet.y_end), 2)

def draw_enemy(enemy):
    pygame.draw.circle(window, enemy.color, (enemy.x, enemy.y), 20 ,1)

if __name__ == "__main__":
    game = game.game()
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((game.screen_x,game.screen_y))
    player = player(game)
    player.rotate((45+180)*(math.pi/180))
    enemies = []
    level = 1
    intervals = [600]
    difficulty = 80
    last_enemy_ctime = 0
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
        gameStarted = True

        window.fill((0,0,0))
        
        draw_player(player, game.screen_x/2, game.screen_y/2)
        for bullet in player.bullets:
            bullet.move()
            draw_bullet(bullet, game.screen_x/2, game.screen_y/2)

        for zombi in enemies:
            zombi.move()
            draw_enemy(zombi)
            player.check_enemy_hit(zombi)

        #pygame.draw.circle(window,(255,0,0),(800, 450), 30, 1)

        if (GAME_TIME.get_ticks() - last_enemy_ctime > intervals[level-1]) and (gameStarted is True):
            enemies.append( enemy.enemy(game.screen_x, game.screen_y) )
            last_enemy_ctime= GAME_TIME.get_ticks()
        
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
                    player.shoot(game.screen_x/2, game.screen_y/2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False

        clock.tick(60)

        pygame.display.update()