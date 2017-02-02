import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
from player import player
import enemy
import game
import math
from time import sleep
import drawing

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
    pygame.draw.circle(window, enemy.color, (math.ceil(enemy.x), math.ceil(enemy.y)), 20 ,1)

def update_game():
    window.fill((0,0,0))
    
    draw_player(player, game.screen_x/2, game.screen_y/2)
    
    for bullet in player.bullets:
        bullet.move()
        draw_bullet(bullet, game.screen_x/2, game.screen_y/2)

    for idx, zombi in enumerate(enemies):
        zombi.move()
        zombi.check_player_reachable(50, player)
        draw_enemy(zombi)
        if player.check_enemy_hit(zombi):
            del enemies[idx]

def show_HUD(player, game):
    #score
    drawing.print_text(window, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", (10,10), 3, 30, (255,255,255))


    # lives
    space = 10
    for live in range(player.lives):
        pygame.draw.lines(window,(255,0,0), True, [(5+space+(30+space)*live,0+(game.screen_y-space-30)),((10+space)+(30+space)*live,0+(game.screen_y-space-30)),
            ((15+space)+(30+space)*live,5+(game.screen_y-space-30)),((20+space)+(30+space)*live,0+(game.screen_y-space-30)),((25+space)+(30+space)*live,0+(game.screen_y-space-30)),
            ((30+space)+(30+space)*live,5+(game.screen_y-space-30)),((30+space)+(30+space)*live,10+(game.screen_y-space-30)),((15+space)+(30+space)*live,25+(game.screen_y-space-30)),
            ((0+space)+(30+space)*live,10+(game.screen_y-space-30)),((0+space)+(30+space)*live,5+(game.screen_y-space-30))], 3)

def show_menu(name, items):
    pygame.draw.circle(window,(255,0,0),(800, 450), 30, 1)
    #pygame.draw.circle(window, (255,0,0), (game.screen_x/2, game.screen_y/2), 80, 1)

def pause_game(enemy_time,pause):
    time = GAME_TIME.get_ticks() - enemy_time
    while pause:
        window.fill((0,0,0))
        menu = ["return, settings, score, quit"]
        show_menu("PAUSE", menu)
        for event in GAME_EVENTS.get():    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pause = False;
                    enemy_time = (GAME_TIME.get_ticks() + time)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    chosen +=1
                    if chosen > len(menu):
                        chosen = 0
                if event.key == pygame.K_UP:
                    chosen -= 1
                    if chosen < 0:
                        chosen = len(menu)

            if event.type == GAME_GLOBALS.QUIT:
                    pygame.quit()
                    sys.exit()

        clock.tick(60)

        pygame.display.update()

if __name__ == "__main__":
    game = game.game()
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((game.screen_x,game.screen_y))
    player = player(game)
    player.rotate((45+180)*(math.pi/180))
    enemies = []
    level = 1
    intervals = [2000]
    last_enemy_ctime = 0
    gameStarted = False
    pause = False
    left = False
    right = False
    shoot = False
    gameStarted = True

    while True:
        
        update_game()
        #pygame.draw.circle(window,(255,0,0),(800, 450), 30, 1)

        if (GAME_TIME.get_ticks() - last_enemy_ctime > intervals[level-1]) and (gameStarted is True):
            enemies.append( enemy.enemy(game) )
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
                if event.key == pygame.K_ESCAPE:
                    pause = True
                if event.key == pygame.K_LEFT:    
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_SPACE:
                    player.shoot(game.screen_x/2, game.screen_y/2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    print("pred: ", last_enemy_ctime)
                    pause_game(last_enemy_ctime, pause)
                    print("po: ", last_enemy_ctime)
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False

        clock.tick(60)
        
        show_HUD(player, game)

        pygame.display.update()