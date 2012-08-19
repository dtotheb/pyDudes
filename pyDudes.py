#!/usr/bin/python
import sys
import pygame
from pygame.locals import *
from helpers import *
from Dude import Dude
from Alien import Alien

#setup pygame
pygame.init()

#setup the window
MAXWIDTH = 500
MAXHEIGHT = 500
screen = pygame.display.set_mode((MAXWIDTH, MAXHEIGHT), 0, 32)
pygame.display.set_caption('Py Dudes')
pygame.mouse.set_visible(0)

#setup the background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

#Draw Everything
screen.blit(background, (0, 0))
pygame.display.flip()




#setup the sprites/clock
allsprites = pygame.sprite.LayeredDirty()
rects = allsprites.draw(screen)
pygame.display.update(rects)
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)

#setup the Dude
dude = Dude()
dude.rect.center = (MAXWIDTH / 2, MAXHEIGHT / 2)
allsprites.add(dude)


#setup some Aiens to shoot at
aliens = pygame.sprite.Group()
for n in range(1, 5):
    alien = Alien()
    alien.rect.center = (MAXWIDTH / 5 * n, 50)
    aliens.add(alien)

allsprites.add(aliens)


def fire():
    bullet = dude.shoot()
    bullets.add(bullet)

bullets = pygame.sprite.Group()

#run the game loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Check for arrow keys being pushed
        # and set the Dude's moving direction
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dude.moving = 'right'
            elif event.key == pygame.K_LEFT:
                dude.moving = 'left'
            elif event.key == pygame.K_UP:
                dude.moving = 'up'
            elif event.key == pygame.K_DOWN:
                dude.moving = 'down'
            elif event.key == pygame.K_SPACE:
                fire()
        elif event.type == pygame.KEYUP:
            dude.moving = False

    bullets.update()
    allsprites.update()

    pygame.sprite.groupcollide(bullets,aliens, True, True)

    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    bullets.draw(screen)
    pygame.display.flip()
