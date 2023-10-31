import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

new_game = True

font = pygame.font.Font('assets/Pixeltype.ttf', 50)

run = True
SCREEN_WIDTH = 1058
SCREEN_HEIGHT = 280

pygame.display.set_caption('DinoGame')

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
bg_surface = pygame.image.load('assets/bg.png').convert()

game_over = font.render('GAME OVER', False, 'Black')

fscore = font.render('final score', False, 'Black')
fscore_rect = fscore.get_rect(center = (525, 100))


score = font.render('Score:', False, 'Black')
score_rect = score.get_rect(topleft = (900, 20))

cact_img = pygame.image.load('assets/cactus.png').convert_alpha()
cact = pygame.transform.scale(cact_img, (40, 60)).convert_alpha()
cactxpos = 900
cactus_hb = cact.get_rect(midbottom = (cactxpos,225))


player_img = pygame.image.load('assets/dino0.png').convert_alpha()
player = pygame.transform.scale(player_img, (55, 60)).convert_alpha()
player_hb = player.get_rect(midbottom = (100, 225))

player_grav = 0

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

    if(new_game):
        screen.fill((0, 0, 0))
        screen.blit(bg_surface,(0, 0))

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
            cactus_hb.left = player_hb.right
            screen.blit(game_over, (450, 50))
            new_game = False
        
        screen.blit(score, score_rect)

    else:
        
        screen.blit(fscore, fscore_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()