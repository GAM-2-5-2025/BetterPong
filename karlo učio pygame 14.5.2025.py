import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Trouble Maker')
clock = pygame.time.Clock()
test_font = pygame.font.Font('UltimatePygameIntro-main/font/Pixeltype.ttf', 50)

screen.fill('White')

sky_surface = pygame.image.load('UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surface = pygame.image.load('UltimatePygameIntro-main/graphics/ground.png').convert()
text_surface = test_font.render('Dobar dan HRVATSKA', False, 'Blue')
snail_surface = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
player_surf = pygame.image.load('UltimatePygameIntro-main/graphics/player/player_walk_1.png').convert_alpha()
#player_rect = pygame.Ract

mjeraludila = pygame.Surface((200,35))
mjeraludila.fill('Blue')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,100))
    screen.blit(snail_surface, (snail_x_pos, 250))
    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 600
        
    screen.blit(player_surf,(80,200))
    

    screen.blit(mjeraludila, (600,0))
    
    pygame.display.update()
    clock.tick(60)

