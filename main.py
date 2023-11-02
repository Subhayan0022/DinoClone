import pygame
import sys

def scoring():
    time = int(pygame.time.get_ticks()/1000) - starttime
    score = font.render(f'Score : {time}', False, 'Black')
    score_rect = score.get_rect(topleft = (880, 20))
    screen.blit(score, score_rect)
    return time

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
cactxpos = 900
cactus_hb = cact.get_rect(midbottom = (cactxpos,225))


player_img = pygame.image.load('assets/dino0.png').convert_alpha()
player = pygame.transform.scale(player_img, (55, 60)).convert_alpha()
player_hb = player.get_rect(midbottom = (100, 225))

player_grav = 0

enemy_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_spawn, 900)

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
                cactus_hb.x = cactxpos
                starttime = int(pygame.time.get_ticks() / 1000)

        if (event.type == enemy_spawn) and new_game:
            print("TEST")
            

    if(new_game):
        screen.fill((0, 0, 0))
        screen.blit(bg_surface,(0, 0))

        finalscore = scoring()

        cactus_hb.x -= 5
        if (cactus_hb.right <= 0):
            cactus_hb.left = 1058
        screen.blit(cact, cactus_hb)

        player_grav +=1
        player_hb.y += player_grav
        screen.blit(player,player_hb)

        if(player_hb.bottom >= 225):
            player_hb.bottom = 225
            player_grav = 0
        
        if(cactus_hb.colliderect(player_hb) == 1):
            new_game = False
        
    else:
        fscore = font.render(f'You got : {finalscore}', False, 'Black')
        fscore_rect = fscore.get_rect(center = (525, 100))
        
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