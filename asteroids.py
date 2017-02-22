import pygame

import sys
import random
entity_color = (255, 255, 255,255)
listAsteroid=[]
listLaser=[]
leveltime=50
creationTime=leveltime
all_sprites_list = pygame.sprite.Group()
lives=3
score=0


#----------------------------------------------
#CLASSES
#----------------------------------------------
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Ship(Entity):
    def __init__(self, x, y, width, height):
        super(Ship, self).__init__(x, y, width, height)
        self.image = pygame.Surface([self.width, self.height])
        ship = pygame.image.load('ship.png')
        self.image.blit(ship, (0, 0))



class Player(Ship):
    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)
        self.y_change = 0
        self.y_dist = 5

    def MoveKeyDown(self, key):
        if (key == pygame.K_SPACE):
            x = Laser(player.rect.x + 20, player.rect.y + 18, 5, 2)
            all_sprites_list.add(x)
            listLaser.append(x)
        elif (key == pygame.K_UP):
            self.y_change += -self.y_dist

        elif (key == pygame.K_DOWN):
            self.y_change += self.y_dist

    def MoveKeyUp(self, key):
        if (key == pygame.K_UP):
            self.y_change += self.y_dist
        elif (key == pygame.K_DOWN):
            self.y_change += -self.y_dist

    def update(self):
        self.rect.move_ip(0, self.y_change)
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > window_height - self.height:
            self.rect.y = window_height - self.height


class Asteroid(Entity):

    def __init__(self, x, y, width, height):
        super(Asteroid, self).__init__(x, y, width, height)
        self.image = pygame.Surface([width, height])
        self.image.fill(entity_color)
        self.x_direction = 5
        self.speed = 5

    def update(self):
        self.rect.x-=5

class Laser(Entity):
    def __init__(self,x, y, width, height):
        super(Laser, self).__init__(x, y, width, height)
        self.image = pygame.Surface([5, 2])
        self.image.fill(entity_color)
        self.x_direction = 5
        self.speed = 5

    def update(self):
        self.rect.x+=5


#FUNCTIONS

def checkScreen(asteroids,lasers):
    for i in asteroids:
        if i.rect.x<=0:
            i.remove(all_sprites_list)
            asteroids.remove(i)
    for i in lasers:
        if i.rect.x>=700:
            i.remove(all_sprites_list)
            lasers.remove(i)

def checkKill(all):
    global lives
    for i in all:
        if i.rect.colliderect(player.rect):
            all.remove(i)
            i.remove(all_sprites_list)
            killed=True
            print('dead')
            lives-=1
            print(lives)
def laserHit(asteroids,lasers):
    for i in asteroids:
        for x in listLaser:
            if i.rect.colliderect(x):
                i.remove(all_sprites_list)
                x.remove(all_sprites_list)
                asteroids.remove(i)
                lasers.remove(x)

#---------------------------------------------------------

pygame.init()

window_width = 700
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteroids")

clock = pygame.time.Clock()

First = Asteroid(window_width, random.randint(10,window_height-10), 20, 20)
listAsteroid.append(First)
player = Player(20, window_height / 2, 40, 37)

all_sprites_list.add(First)
all_sprites_list.add(player)

fontObj = pygame.font.Font('freesansbold.ttf', 26)
textSurfaceObj = fontObj.render(str(lives), True,(255,255,255))
textRectObj=textSurfaceObj.get_rect()

while True:
    screen.blit(textSurfaceObj,textRectObj)
    laserHit(listAsteroid,listLaser) #laser hits asteroid
    checkKill(listAsteroid) #player hit by asteroid
    checkScreen(listAsteroid,listLaser) #if anything off screen
    if creationTime<=0:#create asteroids after set amount of time
        x=Asteroid(window_width-1, random.randint(0,window_height-20), 20, 20)
        listAsteroid.append(x)
        all_sprites_list.add(x)
        leveltime-=1 #each asteroid is formed make it shorter until next is made
        creationTime=leveltime
        print(len(listAsteroid))
    # Event processing here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            player.MoveKeyDown(event.key)
        elif event.type == pygame.KEYUP:
            player.MoveKeyUp(event.key)

    for ent in all_sprites_list:
        ent.update()


    all_sprites_list.draw(screen)
    creationTime-=1
    pygame.display.flip()

    clock.tick(60)