import pygame
from sys import exit

pygame.init()
gamex = 900
gamey = 1000
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
l1r = l1.get_rect(topleft = (0, 0))
l1.fill("Red")
l2 = pygame.Surface((bordersize, gamey))
l2r = l2.get_rect(topleft = (0, 0))
l2.fill("Purple")
l3 = pygame.Surface((gamex, bordersize))
l3r = l3.get_rect(topleft = (0, gamey - bordersize))
l3.fill("Blue")
l4 = pygame.Surface((bordersize, gamey))
l4r = l4.get_rect(topleft = (gamex - bordersize, 0))
l4.fill("Pink")

w1 = pygame.Surface((gamex - 2 * bordersize, 100))
w1r = w1.get_rect(topleft = (bordersize, 200))

#player area
paposy = 500
pay = 400
pa = pygame.Surface((gamex - 2 * bordersize, pay))
pa.fill("Lightblue")


# player
playerspeed = 6
V = []
pv = ''

playerx = 100
playery = 20
p1 = pygame.Surface((playerx, playery))
p1.fill("Blue")

px = gamex // 2 - playerx // 2
py = paposy + pay // 2 - playery // 2
p1r = p1.get_rect(topleft = (px, py))

# ball
ballspeed = 10
bv = ''

b = pygame.Surface((10, 10))
b.fill("Green")
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
        screen.blit(l1, l1r)
        screen.blit(l2, l2r)
        screen.blit(l3, l3r)
        screen.blit(l4, l4r)

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
        screen.blit(l1, l1r)
        screen.blit(l2, l2r)
        screen.blit(l3, l3r)
        screen.blit(l4, l4r)

        screen.blit(w1, w1r)


        #PLAYER AREA CONSTRICTIONS
        screen.blit(pa, (bordersize, paposy))

        if p1r.x >= gamex - playerx - bordersize:
            p1r.x = gamex - playerx - bordersize
        if p1r.x <= bordersize:
            p1r.x = bordersize
        if p1r.y >= paposy + pay - playery:
            p1r.y = paposy + pay - playery
        if p1r.y <= paposy:
            p1r.y = paposy

        # Player
        screen.blit(p1, p1r)

        if len(V) >= 3:
            V = [V[-2], V[-1]]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            p1r.x += playerspeed
            V.append('right')
            if len(V) >= 3:
                V = [V[-2], V[-1]]
                if V[0] and V[1] == 'up':
                    pv = 'up'
                if V[0] and V[1] == 'down':
                    pv = 'down'
                if V[0] and V[1] == 'left':
                    pv = 'left'
                if V[0] and V[1] == 'right':
                    pv = 'right'
                if (V[0] == 'right' and V[1] == 'up') or (V[1] == 'right' and V[0] == 'up'):
                    pv = 'up right'
                if (V[0] == 'left' and V[1] == 'up') or (V[1] == 'left' and V[0] == 'up'):
                    pv = 'up left'
                if (V[0] == 'right' and V[1] == 'down') or (V[1] == 'right' and V[0] == 'down'):
                    pv = 'down right'
                if (V[0] == 'left' and V[1] == 'down') or (V[1] == 'left' and V[0] == 'down'):
                    pv = 'down left'
        if keys[pygame.K_a]:
            p1r.x -= playerspeed
            V.append('left')
            if len(V) >= 3:
                V = [V[-2], V[-1]]
                if V[0] and V[1] == 'up':
                    pv = 'up'
                if V[0] and V[1] == 'down':
                    pv = 'down'
                if V[0] and V[1] == 'left':
                    pv = 'left'
                if V[0] and V[1] == 'right':
                    pv = 'right'
                if (V[0] == 'right' and V[1] == 'up') or (V[1] == 'right' and V[0] == 'up'):
                    pv = 'up right'
                if (V[0] == 'left' and V[1] == 'up') or (V[1] == 'left' and V[0] == 'up'):
                    pv = 'up left'
                if (V[0] == 'right' and V[1] == 'down') or (V[1] == 'right' and V[0] == 'down'):
                    pv = 'down right'
                if (V[0] == 'left' and V[1] == 'down') or (V[1] == 'left' and V[0] == 'down'):
                    pv = 'down left'
        if keys[pygame.K_s]:
            p1r.y += playerspeed
            V.append('down')
            if len(V) >= 3:
                V = [V[-2], V[-1]]
                if V[0] and V[1] == 'up':
                    pv = 'up'
                if V[0] and V[1] == 'down':
                    pv = 'down'
                if V[0] and V[1] == 'left':
                    pv = 'left'
                if V[0] and V[1] == 'right':
                    pv = 'right'
                if (V[0] == 'right' and V[1] == 'up') or (V[1] == 'right' and V[0] == 'up'):
                    pv = 'up right'
                if (V[0] == 'left' and V[1] == 'up') or (V[1] == 'left' and V[0] == 'up'):
                    pv = 'up left'
                if (V[0] == 'right' and V[1] == 'down') or (V[1] == 'right' and V[0] == 'down'):
                    pv = 'down right'
                if (V[0] == 'left' and V[1] == 'down') or (V[1] == 'left' and V[0] == 'down'):
                    pv = 'down left'
        if keys[pygame.K_w]:
            p1r.y -= playerspeed
            V.append('up')
            if len(V) >= 3:
                V = [V[-2], V[-1]]
                if V[0] and V[1] == 'up':
                    pv = 'up'
                if V[0] and V[1] == 'down':
                    pv = 'down'
                if V[0] and V[1] == 'left':
                    pv = 'left'
                if V[0] and V[1] == 'right':
                    pv = 'right'
                if (V[0] == 'right' and V[1] == 'up') or (V[1] == 'right' and V[0] == 'up'):
                    pv = 'up right'
                if (V[0] == 'left' and V[1] == 'up') or (V[1] == 'left' and V[0] == 'up'):
                    pv = 'up left'
                if (V[0] == 'right' and V[1] == 'down') or (V[1] == 'right' and V[0] == 'down'):
                    pv = 'down right'
                if (V[0] == 'left' and V[1] == 'down') or (V[1] == 'left' and V[0] == 'down'):
                    pv = 'down left'


        # ball
        screen.blit(b, br)

        if bv == 'up':
            br.y -= ballspeed
        elif bv == 'down':
            br.y += ballspeed
        elif bv == 'left':
            br.x -= ballspeed
        elif bv == 'right':
            br.x += ballspeed
        elif bv == 'up right':
            br.x += ballspeed / round(((2)**0.5), 4)
            br.y -= ballspeed / round(((2)**0.5), 4)
        elif bv == 'down left':
            br.x -= ballspeed / round(((2)**0.5), 4)
            br.y += ballspeed / round(((2)**0.5), 4)
        elif bv == 'down right':
            br.x += ballspeed / round(((2)**0.5), 4)
            br.y += ballspeed / round(((2)**0.5), 4)
        elif bv == 'up left':
            br.x -= ballspeed / round(((2)**0.5), 4)
            br.y -= ballspeed / round(((2)**0.5), 4)


        if br.colliderect(p1r):
            if pv == 'up':
                bv = 'up'
            elif pv == 'right':
                bv = 'right'
            elif pv == 'down':
                bv = 'down'
            elif pv == 'left':
                bv = 'left'
            elif pv == 'up right':
                bv = 'up right'
            elif pv == 'down right':
                bv = 'down right'
            elif pv == 'up left':
                bv = 'up left'
            elif pv == 'down left':
                bv = 'down left'

        # ball upon hitting a wall
        if br.colliderect(w1r):
            if bv == 'up':
                bv = 'down'
            if bv == 'up left':
                bv = 'down left'
            if bv == 'up right':
                bv = 'down right'
        if br.colliderect(l1r): # imam zid pa nikad nece doci do gornje bariere
            bv = ''
        if br.colliderect(l2r):
            if bv == 'left':
                bv = 'right'
            if bv == 'up left':
                bv = 'up right'
            if bv == 'down left':
                bv = 'down right'
        if br.colliderect(l3r):
            if bv == 'down':
                bv = 'up'
            if bv == 'down left':
                bv = 'up left'
            if bv == 'down right':
                bv = 'up right'
        if br.colliderect(l4r):
            if bv == 'right':
                bv = 'left'
            if bv == 'up right':
                bv = 'up left'
            if bv == 'down right':
                bv = 'down left'



        if s == 'game over':
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)