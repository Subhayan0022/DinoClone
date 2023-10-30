import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

run = True
SCREEN_WIDTH = 1058
SCREEN_HEIGHT = 280

pygame.display.set_caption('DinoGame')

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
bg_surface = pygame.image.load('assets/bg.png').convert()

cact_img = pygame.image.load('assets/cactus.png').convert_alpha()
cact = pygame.transform.scale(cact_img, (40, 60)).convert_alpha()
cactxpos = 800
cactus_hb = cact.get_rect(midbottom = (cactxpos,225))


player_img = pygame.image.load('assets/dino0.png').convert_alpha()
player = pygame.transform.scale(player_img, (55, 60)).convert_alpha()
player_hb = player.get_rect(midbottom = (100, 225))

while(run):

    screen.fill((0, 0, 0))
    
    screen.blit(bg_surface,(0, 0))

    cactus_hb.left -= 5
    screen.blit(cact, cactus_hb)
    if(cactus_hb.left<=-30):
        cactus_hb.left = 1020

    screen.blit(player,player_hb)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player_hb.move_ip(0,-5)
    elif key[pygame.K_s] == True:
        player_hb.move_ip(0,5)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    pygame.display.update()
    clock.tick(60)

pygame.quit()