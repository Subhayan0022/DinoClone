import pygame
import sys
from random import randint

def scoring():
    time = int(pygame.time.get_ticks()/1000) - starttime
    score = font.render(f'Score : {time}', False, 'Black')
    score_rect = score.get_rect(topleft = (880, 20))
    screen.blit(score, score_rect)
    return time

def enemy_spawnpoint(enemy_list):
    if(enemy_list):
        for enemy_rect in enemy_list:
            enemy_rect.x -= 5

            if(enemy_rect.bottom == 225):
                screen.blit(cact, enemy_rect)
            else:
                screen.blit(birb_hb, enemy_rect)

        enemy_list = [enemy for enemy in enemy_list if enemy.x > -100]

        return enemy_list
    
    else:
        return []

def enemycollision(player, enemy):
    if(enemy):
        for enemy_rect in enemy:
            if(player.colliderect(enemy_rect)):
                return False

    return True

def dinoanimation():
    global player, Dino_Walk

    if(player_hb.bottom < 225):
        #enter the duck animation here
        player = Dinos[int(Dino_Walk)]

    else:
        Dino_Walk += 0.1
        if(Dino_Walk >= len(Dinos)):
            Dino_Walk = 0

        player = Dinos[int(Dino_Walk)]


pygame.init()

clock = pygame.time.Clock()

new_game = False

starttime = 0

finalscore = 0

font = pygame.font.Font('assets/Pixeltype.ttf', 50)

run = True
SCREEN_WIDTH = 1058
SCREEN_HEIGHT = 280

pygame.display.set_caption('DinoGame')

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
bg_surface = pygame.image.load('assets/bg.png').convert()

game_over = font.render('GAME OVER', False, 'Black')

restart = font.render('Press SPACE to Start', False, 'Black')
restart_rect = restart.get_rect(midbottom = (525, 200))


cact_img = pygame.image.load('assets/cactus.png').convert_alpha()
cact = pygame.transform.scale(cact_img, (40, 60)).convert_alpha()

birb_img1 = pygame.image.load('assets/birb.png').convert_alpha()
birb1 = pygame.transform.scale(birb_img1, (60, 60)).convert_alpha()
birb_img2 = pygame.image.load('assets/birb2.png').convert_alpha()
birb2 = pygame.transform.scale(birb_img2, (60, 60)).convert_alpha()
birbs = [birb1, birb2]
birb_fly = 0
birb_hb = birbs[birb_fly]


enemy_rect_list = []

player_img_1 = pygame.image.load('assets/dino1.png').convert_alpha()
Dino1 = pygame.transform.scale(player_img_1, (55, 60)).convert_alpha()

player_img_2 = pygame.image.load('assets/dino2.png').convert_alpha()
Dino2 = pygame.transform.scale(player_img_2, (55, 60)).convert_alpha()
Dinos = [Dino1, Dino2]
Dino_Walk = 0
player = Dinos[Dino_Walk]
player_hb = player.get_rect(midbottom = (100, 225))
player_grav = 0

enemy_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_spawn, 900)

birb_fly_animation = pygame.USEREVENT + 2
pygame.time.set_timer(birb_fly_animation, 500)

while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        
        if(new_game):
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE and player_hb.bottom == 225):
                    player_grav = -17
        else:
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                new_game = True
                starttime = int(pygame.time.get_ticks() / 1000)

        if new_game:
            if (event.type == enemy_spawn):
                if(randint(0, 2)):
                    enemy_rect_list.append(cact.get_rect(midbottom = (randint(1058, 1200),225)))
                else:
                    enemy_rect_list.append(birb_hb.get_rect(midbottom = (randint(1058, 1200),150)))
            if (event.type == birb_fly_animation):
                if birb_fly == 0:
                    birb_fly = 1
                else:
                    birb_fly = 0
                birb_hb = birbs[birb_fly] 

            

    if(new_game):
        screen.fill((0, 0, 0))
        screen.blit(bg_surface,(0, 0))

        finalscore = scoring()

        player_grav +=1
        player_hb.y += player_grav

        dinoanimation()

        screen.blit(player,player_hb)

        if(player_hb.bottom >= 225):
            player_hb.bottom = 225
            player_grav = 0

        enemy_rect_list = enemy_spawnpoint(enemy_rect_list)
        
        new_game = enemycollision(player_hb, enemy_rect_list)
        
    else:
        fscore = font.render(f'You got : {finalscore}', False, 'Black')
        fscore_rect = fscore.get_rect(center = (525, 100))

        enemy_rect_list.clear()
        player_hb.midbottom = (100,225)
        player_grav = 0
        
        if(finalscore == 0):
            screen.blit(bg_surface,(0, 0))
            screen.blit(restart, restart_rect)
        else:
            screen.blit(bg_surface,(0, 0))
            screen.blit(game_over, (450, 50))
            screen.blit(fscore, fscore_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()