import pygame
from sys import exit

pygame.init()
gamex = 700
gamey = 800
screen = pygame.display.set_mode((gamex, gamey))
pygame.display.set_caption('Better pong!')
clock = pygame.time.Clock()
s = 'menu'

screen.fill('White')

# MENU SCREEN
m1x = 150
m1y = 200
m1 = pygame.image.load('pixil-frame-0.png')
m1r = m1.get_rect(topleft = (m1x, m1y))
m2 = pygame.image.load('quit.png')
m2r = m2.get_rect(topleft = (m1x + 400, m1y))

# Text
font = pygame.font.Font('Pixeltype.ttf', 100)
text = font.render('BETTER PONG!', True, pygame.Color('Black'))

# MOUSE
mp = 0, 0

# LEVEL
b1 = pygame.Surface((gamex, gamey))
b1.fill('White')

bordersize = 20
l1 = pygame.Surface((gamex, bordersize))
l1.fill("Red")
l2 = pygame.Surface((bordersize, gamey))
l2.fill("Red")
l3 = pygame.Surface((gamex, bordersize))
l3.fill("Red")
l4 = pygame.Surface((bordersize, gamey))
l4.fill("Red")

#player area
paposy = 500
pay = 200
pa = pygame.Surface((gamex - 2 * bordersize, pay))
pa.fill("Lightblue")


# player
playerspeed = 6
V = []

playerx = 100
playery = 20
p1 = pygame.Surface((playerx, playery))
p1.fill("Blue")

px = gamex // 2 - playerx // 2
py = paposy + pay // 2 - playery // 2
p1r = p1.get_rect(topleft = (px, py))

# ball
ballspeed = 10
bsx = 0
bsy = 0

b = pygame.Surface((10, 10))
b.fill("Black")
brx, bry = px + playerx / 2, py - 50
br = b.get_rect(topleft = (brx, bry))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # MOUSE
        if event.type == pygame.MOUSEMOTION:
            mp = event.pos

    if s == 'menu':
        # LEVEL
        screen.blit(b1, (0, 0))
        screen.blit(l1, (0, 0))
        screen.blit(l2, (0, 0))
        screen.blit(l3, (0, gamey - bordersize))
        screen.blit(l4, (gamex - bordersize, 0))

        # MENU SCREEN
        screen.blit(text, (gamex //2 - 200, m1y - 100 ))

        screen.blit(m1, m1r)
        screen.blit(m2, m2r)
        if m1r.collidepoint(mp) and pygame.mouse.get_pressed()[0] == True:
            print('Better pong!')
            s = 'game active'
            pygame.time.wait(250)
        if m2r.collidepoint(mp) and pygame.mouse.get_pressed()[0] == True:
            s = 'game over'
            pygame.time.wait(250)

    if s == 'game active':
        # LEVEL
        screen.blit(b1, (0, 0))
        screen.blit(l1, (0, 0))
        screen.blit(l2, (0, 0))
        screen.blit(l3, (0, gamey - bordersize))
        screen.blit(l4, (gamex - bordersize, 0))


        #PLAYER AREA CONSTRICTIONS
        screen.blit(pa, (bordersize, paposy))

        if px >= gamex - playerx - bordersize:
            px = gamex - playerx - bordersize
        if px <= bordersize:
            px = bordersize
        if py >= paposy + pay - playery:
            py = paposy + pay - playery
        if py <= paposy:
            py = paposy

        # Player
        p1r = p1.get_rect(topleft=(px, py))
        screen.blit(p1, p1r)

        if len(V) >= 3:
            V = [V[-1], V[-2]]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            px += playerspeed
            V.append('right')
        if keys[pygame.K_a]:
            px -= playerspeed
            V.append('left')
        if keys[pygame.K_s]:
            py += playerspeed
            V.append('down')
        if keys[pygame.K_w]:
            py -= playerspeed
            V.append('up')
        print(V)

        # balls
        screen.blit(b, (brx + bsx, bry + bsy))

        if br.colliderect(p1r):
            print("colide")

            if V[0] and V[1] == 'up':
                bsy -= 10


    if s == 'game over':
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)