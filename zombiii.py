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
import functools

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
    pygame.draw.circle(window, enemy.color, (int(math.ceil(enemy.x)), int(math.ceil(enemy.y))), 20 ,1)

def update_game():
    window.fill((0,0,0))
    time = GAME_TIME.get_ticks()
    draw_player(player, game.screen_x/2, game.screen_y/2)

    for bullet in player.bullets:
        bullet.move()
        draw_bullet(bullet, game.screen_x/2, game.screen_y/2)

    for idx, zombi in enumerate(enemies):
        zombi.move(player, time)
        zombi.check_player_reachable(50, player, time)
        draw_enemy(zombi)
        if player.check_enemy_hit(zombi):
            del enemies[idx]

def show_HUD(player, game):
    #score
    size = 30
    color = (255,255,255)
    thickness = 3
    space = 10
    drawing.print_text(window, str(game.score), (space,space), thickness, size, color)
    # lives
    for live in range(player.lives):
        pygame.draw.lines(window,(255,0,0), True, [(5+space+(30+space)*live,0+(game.screen_y-space-30)),((10+space)+(30+space)*live,0+(game.screen_y-space-30)),
            ((15+space)+(30+space)*live,5+(game.screen_y-space-30)),((20+space)+(30+space)*live,0+(game.screen_y-space-30)),((25+space)+(30+space)*live,0+(game.screen_y-space-30)),
            ((30+space)+(30+space)*live,5+(game.screen_y-space-30)),((30+space)+(30+space)*live,10+(game.screen_y-space-30)),((15+space)+(30+space)*live,25+(game.screen_y-space-30)),
            ((0+space)+(30+space)*live,10+(game.screen_y-space-30)),((0+space)+(30+space)*live,5+(game.screen_y-space-30))], thickness)
    # developer
    if(show_dev):
        enemies_cnt = str(len(enemies))
        bullets_cnt = str(len(player.bullets))
        drawing.print_text(window, "ENEMIES: "+enemies_cnt, (game.screen_x - size*(15) + space,10), thickness, size, color)
        drawing.print_text(window, "BULLETS: "+bullets_cnt, (game.screen_x - size*(15) + space,10+size+space), thickness, size, color)
        drawing.print_text(window, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.!:?", (space,game.screen_y-(size+space)*3), thickness, size, color)
        drawing.print_text(window, "LIVES: "+str(player.lives), (space,game.screen_y-(size+space)*2), thickness, size, color)



def draw_menu(game, name, items, chosen):
    space = 10
    name_color = (0,255,0)
    name_thickness = 8
    name_size = 50
    size = 30
    color = (255,255,255)
    chosen_color = (20,255,20)
    chosen_thickness = 4
    thickness = 3
    drawing.print_text(window, name, ((game.screen_x-(len(name)*name_size))/2,((game.screen_y)/2-name_size-(len(items)*(size+space)-space))), name_thickness, name_size, name_color)

    for idx, item in enumerate(items):
        if idx == chosen:
            drawing.print_text(window, item, ((game.screen_x-(len(item)*size))/2,((game.screen_y)/2-name_size-(len(items)*(size+space))+space)+name_size+space*2+ (size+space)*idx), chosen_thickness, size, chosen_color)
        else:
            drawing.print_text(window, item, ((game.screen_x-(len(item)*size))/2,((game.screen_y)/2-name_size-(len(items)*(size+space))+space)+name_size+space*2+ (size+space)*idx), thickness, size, color)

def pause_game(game, enemy_time):
    time = GAME_TIME.get_ticks() - enemy_time

    show_menu_screen(game, "PAUSE", (
        # as game is not a global object, we need to pass it to the fake_score method
        ("gain score", functools.partial(fake_score, game)),
        # another way to 'postpone' the method call. You decide what suits you best
        ("settings",  lambda: show_menu_screen(game, "SETTINGS",
            (
                ("Display", lambda: "Show Display settings"),
                ("Sound", lambda: "Show Sound settings")
            )
        )),
        ("quit", quit_game),
        )
    )

    enemy_time = (GAME_TIME.get_ticks() + time)


def fake_score(game):
    game.score += 1
    game.score *= 10
    return "New score is %s" % game.score

def quit_game():
    pygame.quit()
    sys.exit()

def show_menu_screen(game, name, items):
    menu_items = (('return', lambda: None),) + items
    menu_strs = [i[0] for i in menu_items]
    menu_map = dict(menu_items)

    run = True
    chosen = 0
    while run:
        window.fill((0,0,0))

        draw_menu(game, name, menu_strs, chosen)

        for event in GAME_EVENTS.get():
            if event.type == pygame.KEYUP:

                # common code to handle going back
                if event.key == pygame.K_ESCAPE:
                    run = False;
                    break
                if event.key == pygame.K_RETURN:
                    if menu_strs[chosen] == 'return':
                        run = False
                        break
                    # now handle the menu actions
                    #  the print is not necessary, but the actions do not really do anything yet
                    #  so this is the only way to show off that different methods are called
                    print menu_map[menu_strs[chosen]]()

            # handles changing the selected item
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    chosen +=1
                    if chosen >= len(menu_strs):
                        chosen = 0
                if event.key == pygame.K_UP:
                    chosen -= 1
                    if chosen < 0:
                        chosen = len(menu_strs)-1

            if event.type == GAME_GLOBALS.QUIT:
                quit_game()

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
    show_dev = False
    while True:

        update_game()

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
                    pause_game(game, last_enemy_ctime)
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_SEMICOLON:
                    if show_dev:
                        show_dev = False
                    else:
                        show_dev = True
        if player.lives == 0:
            #save score,etc
            break
        clock.tick(60)

        show_HUD(player, game)

        pygame.display.update()
