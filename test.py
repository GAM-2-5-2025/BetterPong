import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Fake Trouble Maker')
clock = pygame.time.Clock()
"""test_font = pygame.font.Font('UltimatePygameIntro-main/font/Pixeltype.ttf', 50)"""

screen.fill('White')

#LEVEL
b1 = pygame.Surface((1200, 600))
b1.fill('White')
l1 = pygame.Surface((1200, 50))
l1.fill("Red")
l2 = pygame.Surface((50, 600))
l2.fill("Red")
l3 = pygame.Surface((1200,50))
l3.fill("Red")
l4 = pygame.Surface((50, 600))
l4.fill("Red")

#player

p1 = pygame.Surface((60,60))
p1.fill("Blue")

"""sky_surface = pygame.image.load('UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surface = pygame.image.load('UltimatePygameIntro-main/graphics/ground.png').convert()
text_surface = test_font.render('Dobar dan HRVATSKA', False, 'Blue')
snail_surface = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
player_surf = pygame.image.load('UltimatePygameIntro-main/graphics/player/player_walk_1.png').convert_alpha()
#player_rect = pygame.Ract

mjeraludila = pygame.Surface((200,35))
mjeraludila.fill('Blue')"""

#player
px = 0
py = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #ovo ne radi ne znam zasto
    '''if event.type == pygame.KEYDOWN:
            if event.key == keys[pyame.K_w]:
                px += 10
            if event.key == keys[pygame.K_s]:
                px -= 10
            if event.key == keys[pygame.K_d]:
                py += 10
            if event.key == keys[pygame.K_a]:
                py -= 10'''
            

    #LEVEL
    screen.blit(b1, (0,0))
    screen.blit(l1,(0,0))
    screen.blit(l2,(0,0))
    screen.blit(l3,(0,550))
    screen.blit(l4,(1150,0))

    #Player
    screen.blit(p1, (570 + px, 270 + py))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        px += 10
    if keys[pygame.K_a]:
        px -= 10
    if keys[pygame.K_s]:
        py += 10
    if keys[pygame.K_w]:
        py -= 10
    
    """screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,100))
    screen.blit(snail_surface, (snail_x_pos, 250))
    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 600
        
    screen.blit(player_surf,(80,200))
    

    screen.blit(mjeraludila, (600,0))"""
    
    pygame.display.update()
    clock.tick(60)
