import pygame
from sys import exit

pygame.init()
gamex = 1100
gamey = 1000
screen = pygame.display.set_mode((gamex, gamey))
pygame.display.set_caption('Better pong!')
clock = pygame.time.Clock()
frame = 0
lastframe = 0
gamestate = 'Start screen'
difficulty = ''
brickskilled = []
livescount = 0


screen.fill('White')

class borders(pygame.sprite.Sprite):
    def __init__(self, col, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(col)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
    def display(self):
        screen.blit(self.image, self.rect)

rect_images = {}
scale = 2
class images(pygame.sprite.Sprite):
    def __init__(self, file, x, y, scaling, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file)
        if scaling:
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (x, y))
        rect_images[file] = self.rect
        self.x = rect_images[file] # sta je ovo
    def display(self):
        screen.blit(self.image, self.rect)

textsepparation = 50
rect_texts = {}
class text(pygame.sprite.Sprite):
    def __init__(self, text, color, x, y, size, font):
        pygame.sprite.Sprite.__init__(self)
        if font == 'n':
            self.font = pygame.font.Font('assets/Pixeltype.ttf', size)
        elif font == 'b':
            self.font = pygame.font.Font('assets/Pixellari.ttf', size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect(topleft = (x, y))
        rect_texts[text] = self.rect
    def display(self):
        screen.blit(self.image, self.rect)
    def newdisplay(self, text, color, x, y, size):
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect(topleft=(x, y))
        screen.blit(self.image, self.rect)

class Infoscreen:
    def __init__(self):
        self.x = 300
        '''if difficulty == 'easy':
            self.lives = 5
        elif difficulty == 'medium':
            self.lives = 3
        elif difficulty == 'hard':
            self.lives = 2
        elif difficulty == 'hardcore':
            self.lives = 1'''
Infoscreen = Infoscreen()

titlex = (gamex - Infoscreen.x) // 2 - 300

coincounter_pos_x = gamex - Infoscreen.x + 20
coincounter_pos_y = 100
coinseparation = 20

# MENU SCREEN
class Menu:
    def __init__(self):
        self.start_pos = (gamex - Infoscreen.x) // 2 - 300, 100
        self.buttonseparation_y = 150
        self.buttonseparation_x = 50
        self.buttonseparation2_y = 100
Menu = Menu()

Playicon = images('assets/play icon.png', Menu.start_pos[0] + 250, Menu.start_pos[1] + Menu.buttonseparation_y, False, 0, 0)
Quiticon = images('assets/quit icon.png', Menu.start_pos[0] + 400 + rect_images['assets/play icon.png'].width + Menu.buttonseparation_x, Menu.start_pos[1] + Menu.buttonseparation_y, False, 0, 0)
Easyicon = images('assets/easy icon.png', Menu.start_pos[0]+ 200 , 550, True, rect_images['assets/play icon.png'].width, rect_images['assets/play icon.png'].height)
Mediumicon = images('assets/medium icon.png', Menu.start_pos[0] + 200 + rect_images['assets/easy icon.png'].width + Menu.buttonseparation_x, 550, True, rect_images['assets/play icon.png'].width, rect_images['assets/play icon.png'].height)
Hardicon = images('assets/hard icon.png', Menu.start_pos[0] + 200 + 2 * (Menu.buttonseparation_x + rect_images['assets/medium icon.png'].width), 550, True, rect_images['assets/play icon.png'].width, rect_images['assets/play icon.png'].height)
Hardcoreicon = images('assets/hardcore icon.png', Menu.start_pos[0] + 200 + 3 * (Menu.buttonseparation_x + rect_images['assets/medium icon.png'].width), 550, True, rect_images['assets/play icon.png'].width, rect_images['assets/play icon.png'].height)
Coinicon = images('assets/coin.png', coincounter_pos_x + 180, 20, True, 100, 100)
Livesicon = images('assets/lives icon.png', coincounter_pos_x + 180, 420, True, 90, 90)
Duckthemeicon = images('assets/duck theme icon.png', Menu.start_pos[0] + 200, 350, True, rect_images['assets/play icon.png'].width, rect_images['assets/play icon.png'].height)
Meadowthemeicon = images('assets/meadow theme icon.png', Menu.start_pos[0] + 200 + rect_images['assets/easy icon.png'].width + Menu.buttonseparation_x, 350, True, rect_images['assets/play icon.png'].width, rect_images['assets/play icon.png'].height)
Portalthemeicon = images('assets/portal theme icon.png', Menu.start_pos[0] + 200 + 2 *  (Menu.buttonseparation_x + rect_images['assets/medium icon.png'].width), 350, True, rect_images['assets/play icon.png'].width, rect_images['assets/play icon.png'].height)
Halloweenthemeicon = images('assets/halloween theme icon.png', Menu.start_pos[0] + 200 + 3 * (Menu.buttonseparation_x + rect_images['assets/medium icon.png'].width), 350, True, rect_images['assets/play icon.png'].width, rect_images['assets/play icon.png'].height)

text_title = text('Better Pong!', 'Black', Menu.start_pos[0] + 50, Menu.start_pos[1], 150, 'b')
text_Coins = text('Coins', 'Gold', coincounter_pos_x, coincounter_pos_y - 50, 100, 'n')
text_coincount = text(f'{len(brickskilled) * 10}', 'Gold', coincounter_pos_x, coincounter_pos_y - 50 + textsepparation, 100, 'n')
text_Lives = text('Lives', 'Red', coincounter_pos_x, 450, 100, 'n')
text_livescount = text(f'{livescount}', 'Red', coincounter_pos_x, 450 + textsepparation, 100, 'n')
text_minuscoins = text('- 150 Coins', 'Black', coincounter_pos_x, 200, 75, 'n')
text_IGNORETODESTROY = text('IGNORE TO DESTROY', 'Red', coincounter_pos_x - 10, 250, 50, 'n')
text_Leaderboard = text('Leaderboard:', 'Gold', coincounter_pos_x, 600, 65, 'n')

text_Theme = text('Theme:', (0,183,255), coincounter_pos_x, 900, 75, 'n')
text_chosentheme = text('Duckies!!!', (0,183,255), coincounter_pos_x, 950, 75, 'n')
chosentheme = ''

text_Themeduck = text('Level:', (0,183,255), coincounter_pos_x, 900, 75, 'n')
text_chosenthemeduck = text('Duckies!!!', (0,183,255), coincounter_pos_x, 950, 75, 'n')
text_Thememeadow = text('Level:', (28, 168, 3), coincounter_pos_x, 900, 75, 'n')
text_chosenthememeadow = text('Meadow lands', (28, 168, 3), coincounter_pos_x - 15, 950, 75, 'n')
text_Themeportal = text('Level:', 'Purple', coincounter_pos_x, 900, 75, 'n')
text_chosenthemeportal = text('Portal madness', 'Purple', coincounter_pos_x, 950, 75, 'n')
text_Themehalloween = text('Level:', 'Orange', coincounter_pos_x, 900, 75, 'n')
text_chosenthemehalloween = text("It's Halloween!!!", 'Orange', coincounter_pos_x, 950, 75, 'n')

text_difez = text('Difficulty:', (49,177, 90), gamex // 2 - 100, 500, 75, 'n')
text_chosendifez = text('Easy', (49,177, 90), gamex // 2 - 100, 550, 75, 'n')
text_difmid = text('Difficulty:', 'Yellow', gamex // 2 - 100, 500, 75, 'n')
text_chosendifmid = text('Medium', 'Yellow', gamex // 2 - 100, 550, 75, 'n')
text_difhard = text('Difficulty:', 'Red', gamex // 2 - 100, 500, 75, 'n')
text_chosendifhard = text('Hard', 'Red', gamex // 2 - 100, 550, 75, 'n')
text_difhardcore = text('Difficulty:', 'Maroon', gamex // 2 - 100, 500, 75, 'n')
text_chosendifhardcore = text('HARDCORE!!!', 'Maroon', gamex // 2 - 100, 550, 75, 'n')

text_mThemeduck = text('Level:', (0,183,255), gamex - 350, 880, 75, 'n')
text_mchosenthemeduck = text('Duckies!!!', (0,183,255), gamex - 350, 930, 75, 'n')
text_mThememeadow = text('Level:', (28, 168, 3), gamex - 350, 880, 75, 'n')
text_mchosenthememeadow = text('Meadow lands', (28, 168, 3),  gamex - 350, 930, 75, 'n')
text_mThemeportal = text('Level:', 'Purple',  gamex - 350, 880, 75, 'n')
text_mchosenthemeportal = text('Portal madness', 'Purple',  gamex - 350, 930, 75, 'n')
text_mThemehalloween = text('Level:', 'Orange',  gamex - 350, 880, 75, 'n')
text_mchosenthemehalloween = text("It's Halloween!!!", 'Orange',  gamex - 350, 930, 75, 'n')

text_leaderboardpos1 = text('1. ImKarlo', 'Gold', coincounter_pos_x, 600 + (0 + 1) * textsepparation, 65, 'n')
text_leaderboardpos2 = text('2. Kira373', 'Gold', coincounter_pos_x, 600 + (1 + 1) * textsepparation, 65, 'n')
text_leaderboardpos3 = text('3. Andrej2008', 'Gold', coincounter_pos_x, 600 + (2 + 1) * textsepparation, 65, 'n')
text_leaderboardpos4 = text('4. AtraMartA', 'Gold', coincounter_pos_x, 600 + (3 + 1) * textsepparation, 65, 'n')
text_leaderboardpos5 = text('5. Tia C.', 'Gold', coincounter_pos_x, 600 + (4 + 1) * textsepparation, 65, 'n')

text_mLeaderboard = text('Leaderboard:', 'Gold', gamex // 2 - 200, 700, 65, 'n')
text_mleaderboardpos1 = text('1. ImKarlo', 'Gold', gamex // 2 - 200, 700 + (0 + 1) * textsepparation, 65, 'n')
text_mleaderboardpos2 = text('2. Kira373', 'Gold', gamex // 2 - 200, 700 + (1 + 1) * textsepparation, 65, 'n')
text_mleaderboardpos3 = text('3. Andrej2008', 'Gold', gamex // 2 - 200, 700 + (2 + 1) * textsepparation, 65, 'n')
text_mleaderboardpos4 = text('4. AtraMartA', 'Gold', gamex // 2 - 200, 700 + (3 + 1) * textsepparation, 65, 'n')
text_mleaderboardpos5 = text('5. Tia C.', 'Gold', gamex // 2 - 200, 700 + (4 + 1) * textsepparation, 65, 'n')

text_Levels = text('Levels:', 'Black', 100, 300, 65, 'n')
text_Difficulties = text('Difficulties:', 'Black', 100, 500, 65, 'n')

Startscreen = images('assets/start screen.png', 0, 0, True, 1100, 1000)
Deathscreen = images('assets/death screen.png', 0, 0, True, 1100, 1000)

#mouse
mouse_pos = 0, 0

#level
background = pygame.Surface((gamex, gamey))
background.fill('White')

bordersize = 20
topwall = pygame.Surface((gamex - Infoscreen.x, bordersize))
rect_topwall = topwall.get_rect(topleft = (0, 0))
topwall.fill("Red")
leftwall = pygame.Surface((bordersize, gamey))
rect_leftwall = leftwall.get_rect(topleft = (0, 0))
leftwall.fill("Purple")
bottomwall = pygame.Surface((gamex - Infoscreen.x, bordersize))
rect_bottomwall = bottomwall.get_rect(topleft = (0, gamey - bordersize))
bottomwall.fill("Blue")
rightwall = pygame.Surface((bordersize, gamey))
rect_rightwall = rightwall.get_rect(topleft = (gamex - bordersize - Infoscreen.x, 0))
rightwall.fill("Pink")

whitecover = borders('White', gamex - 350, gamey - 300, 350, 300)

duckbordertop = borders((0, 183, 239), 0, 0, gamex - Infoscreen.x, bordersize)
duckborderleft = borders((0, 183, 239), 0, 0, bordersize, gamey)
duckborderbottom = borders('Blue', 0, gamey - bordersize, gamex - Infoscreen.x, bordersize)
duckborderright = borders((0, 183, 239), gamex - bordersize - Infoscreen.x, 0, bordersize, gamey)
duckbackground = images('assets/duck background.png', bordersize, bordersize, True, gamex - Infoscreen.x - 2 * bordersize, gamey - 2 * bordersize)

meadowbordertop = images('assets/meadow border horizontal.png', 0, 0, True, gamex - Infoscreen.x, bordersize)
meadowborderleft = images('assets/meadow border vertical.png', 0, 0, True, bordersize, gamey - bordersize)
meadowborderbottom = borders((86, 47, 11), 0, gamey - bordersize, gamex - Infoscreen.x, bordersize)
meadowborderright = images('assets/meadow border vertical.png', gamex - bordersize - Infoscreen.x, 0, True, bordersize, gamey - bordersize)
meadowbackground = images('assets/meadow background.png', bordersize, bordersize, True, gamex - Infoscreen.x - 2 * bordersize, gamey - 2 * bordersize)

portalbordertop = borders((111, 51, 149), 0, 0, gamex - Infoscreen.x, bordersize)
portalborderleft = borders((111, 51, 149), 0, 0, bordersize, gamey)
portalborderbottom = borders('Purple', 0, gamey - bordersize, gamex - Infoscreen.x, bordersize)
portalborderright = borders((111, 51, 149), gamex - bordersize - Infoscreen.x, 0, bordersize, gamey)
portalbackground = images('assets/portal background.png', bordersize, bordersize, True, gamex - Infoscreen.x - 2 * bordersize, gamey - 2 * bordersize)

halloweenbordertop = borders((111, 51, 149), 0, 0, gamex - Infoscreen.x, bordersize)
halloweenborderleft = borders((111, 51, 149), 0, 0, bordersize, gamey)
halloweenborderbottom = borders('Purple', 0, gamey - bordersize, gamex - Infoscreen.x, bordersize)
halloweenborderright = borders((111, 51, 149), gamex - bordersize - Infoscreen.x, 0, bordersize, gamey)
halloweenbackground = images('assets/halloween background.png', bordersize, bordersize, True, gamex - Infoscreen.x - 2 * bordersize, gamey - 2 * bordersize)


class Playerarea(pygame.sprite.Sprite):
    def __init__(self, chosentheme):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (500, 400)
        self.height = 350
        self.image = pygame.Surface((gamex - 2 * bordersize - Infoscreen.x, self.height))
        self.image.fill('Lightblue')
        self.rect = self.image.get_rect(topleft = (bordersize, self.pos[1]))
    def newdisplay(self, chosentheme):
        if chosentheme == 'Duck':
            self.pos = (500, 480)
            self.height = 280
            self.image = pygame.Surface((gamex - 2 * bordersize - Infoscreen.x, self.height))
            self.rect = self.image.get_rect(topleft=(bordersize, self.pos[1]))
            self.image.fill('Lightblue')
        elif chosentheme == 'Meadow':
            self.pos = (500, 550)
            self.height = 250
            self.image = pygame.Surface((gamex - 2 * bordersize - Infoscreen.x, self.height))
            self.rect = self.image.get_rect(topleft=(bordersize, self.pos[1]))
            self.image.fill('Lightblue')
        elif chosentheme == 'Portal':
            print(2)
            self.pos = (500, 550)
            self.height = 300
            self.image = pygame.Surface((gamex - 2 * bordersize - Infoscreen.x, self.height))
            self.rect = self.image.get_rect(topleft=(bordersize, self.pos[1]))
            self.image.fill('Pink')
            self.image.set_alpha(68)
        elif chosentheme == 'Halloween':
            self.pos = (500, 480)
            self.height = 280
            self.image = pygame.Surface((gamex - 2 * bordersize - Infoscreen.x, self.height))
            self.rect = self.image.get_rect(topleft=(bordersize, self.pos[1]))
            self.image.fill('Orange')
            self.image.set_alpha(48)

    def display(self):
        screen.blit(self.image, self.rect)


Playerarea = Playerarea(chosentheme)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 6
        self.velocity = pygame.Vector2()
        self.lastvelocity = pygame.Vector2()
        self.x = 150
        self.y = 35
        self.image = pygame.Surface((self.x, self.y))
        self.image.fill('Blue')
        self.start_pos = ((gamex - Infoscreen.x) // 2 - self.x // 2, Playerarea.pos[0] + Playerarea.height // 2 - self.y // 2)
        self.rect = self.image.get_rect(topleft = self.start_pos)
Player = Player()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.velocity = pygame.Vector2()
        self.powerup = ''
        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill('Green')
        self.pos_x = Player.start_pos[0] + Player.x / 2 - self.size // 2
        self.pos_y = Player.start_pos[1] - 50
        self.wallright = pygame.Surface((1, self.size - 1))
        self.wallbottom = pygame.Surface((self.size, 1))
        self.wallleft = pygame.Surface((1, self.size))
        self.walltop = pygame.Surface((self.size, 1))
        self.rect = self.image.get_rect(topleft = (self.pos_x, self.pos_y))

    def newdisplay(self, chosentheme):
        if chosentheme == 'Duck':
            self.image.fill('Navy')
        elif chosentheme == 'Meadow':
            self.image = images('assets/meadow brick.png', self.pos_x, self.pos_y, True, self.size, self.size).image
        elif chosentheme == 'Halloween':
            self.image = images('assets/halloween ball.png', self.pos_x, self.pos_y, True, self.size, self.size).image
        elif chosentheme == 'Portal':
            self.image.fill('Green')
    def display(self):
        screen.blit(self.image, self.rect)

Ball = Ball()

# BRICKS
rect_bricks = []
bricksize = 20
truebrickskilled = []
class Brick(pygame.sprite.Sprite):
    def __init__(self, brick_pos_x, brick_pos_y, chosentheme):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((bricksize, bricksize))
        if chosentheme == 'Duck':
            self.image = images('assets/duck brick.png', brick_pos_x, brick_pos_y, True, bricksize, bricksize).image
        elif chosentheme == 'Meadow':
            self.image = images('assets/water drop.png', brick_pos_x, brick_pos_y, True, bricksize, bricksize).image # NAPRAVI DA SU KAPLJIVE KISE ISPOD OBLAKA
        elif chosentheme == 'Portal':
            self.image = images('assets/portal brick.png', brick_pos_x, brick_pos_y, True, bricksize, bricksize).image
        elif chosentheme == 'Halloween':
            self.image = images('assets/halloween brick.png', brick_pos_x, brick_pos_y, True, bricksize, bricksize).image

        self.rect = self.image.get_rect(topleft = (brick_pos_x, brick_pos_y))
        rect_bricks.append(self.rect)
    def update(self, c, c1):
        if self.rect.colliderect(Ball.rect):
            if Ball.powerup != 'IGNORE TO DESTROY':
                if self.rect.colliderect(rect_ballwallbottom):
                    Ball.velocity.y = - Ball.velocity.y
                    Ball.rect.y -= 5
                if self.rect.colliderect(rect_ballwallright):
                    Ball.velocity.x = - Ball.velocity.x
                    Ball.rect.x -= 5
                if self.rect.colliderect(rect_ballwallleft):
                    Ball.velocity.x = - Ball.velocity.x
                    Ball.rect.x += 5
                if self.rect.colliderect(rect_ballwalltop):
                    Ball.velocity.y = - Ball.velocity.y
                    Ball.rect.y += 5
                self.kill()
                c.append(1)
                c1.append(1)
            else:
                self.kill()
                c.append(1)
                c1.append(1)


bricksgroup = pygame.sprite.Group()
empty = pygame.sprite.Group()
class Brickfield:
    def __init__(self):
        self.separation = 15
        self.rows = 8
        self.collums = (gamex - 2 * bordersize - Infoscreen.x) // ( bricksize + self.separation )
        self.start = (bordersize + self.separation, bordersize + self.separation)

    def makebrickfield(self, chosentheme):
        if chosentheme == 'Duck':
            for i in range(self.collums):
                for j in range(self.rows + 3):
                    bricksgroup.add(Brick(self.start[0] + i * (bricksize + self.separation), self.start[1] + j * (bricksize + self.separation), chosentheme))
        if chosentheme == 'Meadow':
            for i in range((264 - 50) // (bricksize + self.separation)):
                for j in range(5):
                    bricksgroup.add(Brick(40 + self.start[0] + i * (bricksize + self.separation), 180 + self.start[1] + j * (bricksize + self.separation), chosentheme))
            for i in range((522 - 346) // (bricksize + self.separation)):
                for j in range(5):
                    bricksgroup.add(Brick(320 + self.start[0] + i * (bricksize + self.separation), 320 + self.start[1] + j * (bricksize + self.separation), chosentheme))
            for i in range((721 - 545) // (bricksize + self.separation)):
                for j in range(5):
                    bricksgroup.add(Brick(523 + self.start[0] + i * (bricksize + self.separation), 142 + self.start[1] + j * (bricksize + self.separation), chosentheme))
        if chosentheme == 'Portal':
            for i in range(self.collums):
                for j in range(self.rows + 4):
                    bricksgroup.add(Brick(self.start[0] + i * (bricksize + self.separation), self.start[1] + j * (bricksize + self.separation), chosentheme))
        if chosentheme == 'Halloween':
            for i in range(self.collums):
                for j in range(self.rows + 3):
                    bricksgroup.add(Brick(self.start[0] + i * (bricksize + self.separation), self.start[1] + j * (bricksize + self.separation), chosentheme))
Brickfield = Brickfield()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # MOUSE
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos

    if gamestate == 'Start screen':
        Startscreen.display()

        if rect_images['assets/start screen.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            gamestate = 'Menu'
            pygame.time.wait(40)


    if gamestate == 'Menu':

        if frame == 0:
            # LEVEL
            screen.blit(background, (0, 0))

            # INFOSCREEN
            whitecover.display()
            text_mLeaderboard.display()
            text_mleaderboardpos1.display()
            text_mleaderboardpos2.display()
            text_mleaderboardpos3.display()
            text_mleaderboardpos4.display()
            text_mleaderboardpos5.display()



            # MENU SCREEN
            text_title.display()

            Playicon.display()
            Quiticon.display()

        frame += 1

        if rect_images['assets/play icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            gamestate = 'difficulty selection'
            frame = 0
            pygame.time.wait(250)
        if rect_images['assets/quit icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and frame > 150:
            gamestate = 'game quit'
            frame = 0
            pygame.time.wait(250)

    if gamestate == 'difficulty selection':

        if frame == 0:
            bricksgroup = empty.copy()
            screen.blit(background, (0, 0))
            whitecover.display()

            text_mLeaderboard.display()
            text_mleaderboardpos1.display()
            text_mleaderboardpos2.display()
            text_mleaderboardpos3.display()
            text_mleaderboardpos4.display()
            text_mleaderboardpos5.display()

            text_title.display()
            text_Levels.display()
            text_Difficulties.display()

            Easyicon.display()
            Mediumicon.display()
            Hardicon.display()
            Hardcoreicon.display()
            Duckthemeicon.display()
            Meadowthemeicon.display()
            Portalthemeicon.display()
            Halloweenthemeicon.display()



        frame += 1

        if rect_images['assets/easy icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and chosentheme != '':
            difficulty = 'easy'
            gamestate = 'intro'
            livescount = 5
            frame = 0
            pygame.time.wait(250)
        elif rect_images['assets/medium icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and chosentheme != '':
            difficulty = 'medium'
            gamestate = 'intro'
            livescount = 3
            frame = 0
            pygame.time.wait(250)
        elif rect_images['assets/hard icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and chosentheme != '':
            difficulty = 'hard'
            gamestate = 'intro'
            livescount = 2
            frame = 0
            pygame.time.wait(250)
        elif rect_images['assets/hardcore icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and chosentheme != '':
            difficulty = 'hardcore'
            gamestate = 'intro'
            livescount = 1
            frame = 0
            pygame.time.wait(250)

        if rect_images['assets/duck theme icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            with open('assets/info.txt', 'w') as fin:
                fin.write('Duck')
            with open('assets/info.txt', 'r') as fin:
                chosentheme = fin.readlines()[0]
            pygame.time.wait(300)
        elif rect_images['assets/meadow theme icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            with open('assets/info.txt', 'w') as fin:
                fin.write('Meadow')
            with open('assets/info.txt', 'r') as fin:
                chosentheme = fin.readlines()[0]
            pygame.time.wait(300)
        elif rect_images['assets/portal theme icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            with open('assets/info.txt', 'w') as fin:
                fin.write('Portal')
            with open('assets/info.txt', 'r') as fin:
                chosentheme = fin.readlines()[0]
            pygame.time.wait(300)
        elif rect_images['assets/halloween theme icon.png'].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            with open('assets/info.txt', 'w') as fin:
                fin.write('Halloween')
            with open('assets/info.txt', 'r') as fin:
                chosentheme = fin.readlines()[0]
            pygame.time.wait(300)

        if chosentheme == 'Duck':
            whitecover.display()
            text_mThemeduck.display()
            text_mchosenthemeduck.display()
        elif chosentheme == 'Meadow':
            whitecover.display()
            text_mThememeadow.display()
            text_mchosenthememeadow.display()
        elif chosentheme == 'Portal':
            whitecover.display()
            text_mThemeportal.display()
            text_mchosenthemeportal.display()
        elif chosentheme == 'Halloween':
            whitecover.display()
            text_mThemehalloween.display()
            text_mchosenthemehalloween.display()



    if gamestate == 'intro':
        if frame == 0:
            screen.blit(background, (0, 0))

        if chosentheme == 'Duck':
            text_mThemeduck.display()
            text_mchosenthemeduck.display()
        elif chosentheme == 'Meadow':
            text_mThememeadow.display()
            text_mchosenthememeadow.display()
        elif chosentheme == 'Portal':
            text_mThemeportal.display()
            text_mchosenthemeportal.display()
        elif chosentheme == 'Halloween':
            text_mThemehalloween.display()
            text_mchosenthemehalloween.display()

        if livescount == 5:
            text_difez.display()
            text_chosendifez.display()
        elif livescount == 3:
            text_difmid.display()
            text_chosendifmid.display()
        elif livescount == 2:
            text_difhard.display()
            text_chosendifhard.display()
        elif livescount == 1:
            text_difhardcore.display()
            text_chosendifhardcore.display()

        pygame.display.update()

        pygame.time.wait(1000)
        gamestate = 'game active'

    if gamestate == 'game active':
        # LEVEL
        if frame == 0:
            Player.start_pos = ((gamex - Infoscreen.x) // 2 - Player.x // 2, Playerarea.pos[0] + Playerarea.height // 2 - Player.y // 2 + 60)
            Ball.pos_x = Player.start_pos[0] + Player.x / 2 - Ball.size // 2
            Ball.pos_y = Player.start_pos[1] - 50
            Ball.rect = Ball.image.get_rect(topleft = (Ball.pos_x, Ball.pos_y))
            Player.rect = Player.image.get_rect(topleft = Player.start_pos)
            Ball.velocity = pygame.Vector2(0, 0)
            Player.velocity = pygame.Vector2(0, 0)
            brickskilled = []

        if chosentheme == 'Duck':
            screen.blit(background, (0, 0))
            duckbordertop.display()
            duckborderleft.display()
            duckborderright.display()
            duckborderbottom.display()

            duckbackground.display()

            rect_topwall = duckbordertop.rect
            rect_bottomwall = duckborderbottom.rect
            rect_leftwall = duckborderleft.rect
            rect_rightwall = duckborderright.rect

            if frame == 0:
                Player.image = images('assets/duckplayer.png', Player.rect.topleft[0], Player.rect.topleft[1], True, Player.x, Player.y).image
                Brickfield.makebrickfield(chosentheme)
        elif chosentheme == 'Meadow':
            screen.blit(background, (0, 0))
            meadowbordertop.display()
            meadowborderleft.display()
            meadowborderright.display()
            meadowborderbottom.display()

            meadowbackground.display()

            rect_topwall = meadowbordertop.rect
            rect_bottomwall = meadowborderbottom.rect
            rect_leftwall = meadowborderleft.rect
            rect_rightwall = meadowborderright.rect


            if frame == 0:
                Player.image = images('assets/meadowplayer.png', Player.rect.topleft[0], Player.rect.topleft[1], True, Player.x, Player.y).image
                Brickfield.makebrickfield(chosentheme)

        elif chosentheme == 'Portal':
            screen.blit(background, (0, 0))
            portalbordertop.display()
            portalborderleft.display()
            portalborderright.display()
            portalborderbottom.display()

            portalbackground.display()

            rect_topwall = portalbordertop.rect
            rect_bottomwall = portalborderbottom.rect
            rect_leftwall = portalborderleft.rect
            rect_rightwall = portalborderright.rect

            if frame == 0:
                Player.image = images('assets/portalplayer.png', Player.rect.topleft[0], Player.rect.topleft[1], True, Player.x, Player.y).image
                Brickfield.makebrickfield(chosentheme)

        elif chosentheme == 'Halloween':
            screen.blit(background, (0, 0))
            halloweenbordertop.display()
            halloweenborderleft.display()
            halloweenborderright.display()
            halloweenborderbottom.display()

            halloweenbackground.display()

            rect_topwall = halloweenbordertop.rect
            rect_bottomwall = halloweenborderbottom.rect
            rect_leftwall = halloweenborderleft.rect
            rect_rightwall = halloweenborderright.rect

            if frame == 0:
                Player.image = images('assets/halloweenplayer.png', Player.rect.topleft[0], Player.rect.topleft[1], True, Player.x, Player.y).image
                Brickfield.makebrickfield(chosentheme)

        # INFOSCREEN
        text_Coins.display()
        text_coincount.display()
        text_coincount.newdisplay(f'{len(brickskilled) * 10}', 'Gold', coincounter_pos_x, coincounter_pos_y + textsepparation, 100)
        text_Lives.display()
        text_Leaderboard.display()
        text_leaderboardpos1.display()
        text_leaderboardpos2.display()
        text_leaderboardpos3.display()
        text_leaderboardpos4.display()
        text_leaderboardpos5.display()

        if chosentheme == 'Duck':
            text_Themeduck.display()
            text_chosenthemeduck.display()
            if len(truebrickskilled) >= 0.2 * 21 * 11:
                gamestate = 'game finished'
        elif chosentheme == 'Meadow':
            text_Thememeadow.display()
            text_chosenthememeadow.display()
            if len(truebrickskilled) >= 0.2 * 80:
                gamestate = 'game finished'
        elif chosentheme == 'Portal':
            text_Themeportal.display()
            text_chosenthemeportal.display()
            if len(truebrickskilled) >= 0.2 * 21 * 12:
                gamestate = 'game finished'
        elif chosentheme == 'Halloween':
            text_Themehalloween.display()
            text_chosenthemehalloween.display()
            if len(truebrickskilled) >= 0.2 * 21 * 11:
                gamestate = 'game finished'

        Coinicon.display()
        Livesicon.display()
        text_livescount.newdisplay(f'{livescount}', 'Red', coincounter_pos_x, 470 + textsepparation, 100)
        text_livescount.display()

        if livescount == 0:
            pygame.display.update()
            pygame.time.wait(500)
            gamestate = 'game over'

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if len(brickskilled) >= 15 and Ball.powerup != 'IGNORE TO DESTROY':
                for i in range(15):
                    brickskilled.remove(1)
                Ball.powerup = 'IGNORE TO DESTROY'
                lastframe = frame

        if frame - lastframe < 150 and frame > 150:
            text_minuscoins.display()
            text_IGNORETODESTROY.display()
        else:
            Ball.powerup = ''

        # BRICKS
        bricksgroup.draw(screen)

        #PLAYER AREA CONSTRICTIONS
        if frame == 0:
            Playerarea.newdisplay(chosentheme)
        Playerarea.display()

        if Player.rect.left >= gamex - Player.x - bordersize - Infoscreen.x:
            Player.rect.left = gamex - Player.x - bordersize - Infoscreen.x
        if Player.rect.left <= bordersize:
            Player.rect.left = bordersize
        if Player.rect.bottom >= Playerarea.height + Playerarea.pos[1]:
            Player.rect.bottom = Playerarea.height + Playerarea.pos[1]
        if Player.rect.top <= Playerarea.pos[1]:
            Player.rect.top = Playerarea.pos[1]

        # Player_group
        screen.blit(Player.image, Player.rect)

        xinput = 0
        yinput = 0

        if keys[pygame.K_d]: xinput = 1
        if keys[pygame.K_a]: xinput = -1
        if keys[pygame.K_w]: yinput = -1
        if keys[pygame.K_s]: yinput = 1

        Player.velocity = pygame.Vector2(xinput, yinput)
        if Player.velocity != pygame.Vector2(0, 0):
            Player.velocity = Player.velocity.normalize()
            Player.lastvelocity = Player.velocity

        Player.rect.x += Player.velocity.x * Player.speed
        Player.rect.y += Player.velocity.y * Player.speed

        # ball
        if frame == 0:
            Ball.newdisplay(chosentheme)
        Ball.display()

        rect_ballwallright = Ball.wallright.get_rect(topleft=(Ball.rect.right, Ball.rect.top))
        rect_ballwallbottom = Ball.wallbottom.get_rect(topleft=(Ball.rect.left, Ball.rect.bottom))
        rect_ballwallleft = Ball.wallleft.get_rect(topright=(Ball.rect.left, Ball.rect.top))
        rect_ballwalltop = Ball.walltop.get_rect(bottomleft=(Ball.rect.left, Ball.rect.top))

        bricksgroup.update(brickskilled, truebrickskilled)

        if Ball.rect.colliderect(Player.rect):
            if Player.velocity.y == Ball.velocity.y == -1 and Player.rect.colliderect(rect_ballwalltop):
                Ball.velocity.y = - Ball.velocity.y
                Ball.rect.y += 5
            elif Player.velocity.y == Ball.velocity.y == 1 and Player.rect.colliderect(rect_ballwallbottom):
                Ball.velocity.y = - Ball.velocity.y
                Ball.rect.y -= 5
            elif Player.velocity.x == Ball.velocity.x == 1 and Player.rect.colliderect(rect_ballwallright):
                Ball.velocity.x = - Ball.velocity.x
                Ball.rect.y -= 5
            elif Player.velocity.x == Ball.velocity.x == -1 and Player.rect.colliderect(rect_ballwallleft):
                Ball.velocity.x = - Ball.velocity.x
                Ball.rect.x += 5
            else:
                Ball.velocity = Player.lastvelocity
            if Player.velocity == pygame.Vector2(0, 0):
                if Player.rect.colliderect(rect_ballwallbottom):
                    Ball.velocity.y = - Ball.velocity.y
                    Ball.rect.y -= 5
                if Player.rect.colliderect(rect_ballwallright):
                    Ball.velocity.x = - Ball.velocity.x
                    Ball.rect.x -= 5
                    Ball.rect.y -= 0.2
                if Player.rect.colliderect(rect_ballwallleft):
                    Ball.velocity.x = - Ball.velocity.x
                    Ball.rect.x += 5
                    Ball.rect.y -= 0.2
                if Player.rect.colliderect(rect_ballwalltop):
                    Ball.velocity.y = - Ball.velocity.y
                    Ball.rect.y += 5

        # ball upon hitting a wall
        if Ball.rect.colliderect(rect_bottomwall):
            Ball.velocity.y = - Ball.velocity.y
            Ball.rect.y -= 5
            livescount -= 1
        if Ball.rect.colliderect(rect_topwall):
            Ball.velocity.y = - Ball.velocity.y
            Ball.rect.y += 5
        if Ball.rect.colliderect(rect_leftwall):
            Ball.velocity.x = - Ball.velocity.x
            Ball.rect.x += 5
        if Ball.rect.colliderect(rect_rightwall):
            Ball.velocity.x = - Ball.velocity.x
            Ball.rect.x -= 5

        Ball.rect.x += Ball.velocity.x * Ball.speed
        Ball.rect.y += Ball.velocity.y * Ball.speed

        frame += 1

    if gamestate == 'game quit':
        Deathscreen.display()
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.quit()
        exit()

    if gamestate == 'game finished':
        images('assets/win screen.png', 0, 0, True, 1100, 1000).display()
        pygame.display.update()
        pygame.time.wait(2000)
        gamestate = 'difficulty selection'

        with open('leaderboard.txt', 'a') as fin:
            fin.write(f'')

        frame = 0
        truebrickskilled = []
        Ball.powerup = ''
    if gamestate == 'game over':
        Deathscreen.display()
        pygame.display.update()
        pygame.time.wait(1500)
        frame = 0
        gamestate = 'Menu'

    pygame.display.update()
    clock.tick(60)