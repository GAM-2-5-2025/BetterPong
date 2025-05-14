import pygame
pygame.init()

screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Trouble Maker")

#test slika#
sine_png = pygame.image.load('10V-Sine-Wave-Amplitude.png').convert()

running = True
x = 0
clock = pygame.time.Clock()

while running:
    screen.fill((255, 100, 255))

    screen.blit(sine_png, (x, 30))

    x += 15
    if x > 1500:
        x = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

    delta_time = clock.tick(60) / 10000
    delta_time = max(0.001, min(0.1, delta_time))
    
pygame.quit()
