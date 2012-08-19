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

#setup the sprite groups
bullets = pygame.sprite.Group()
aliens = pygame.sprite.Group()
allsprites = pygame.sprite.LayeredDirty()

#setup the clock
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)

#setup the Dude
dude = Dude()
dude.rect.center = (MAXWIDTH / 2, MAXHEIGHT / 2)
allsprites.add(dude)

#SCORE
SCORE = 0

#setup some Aliens to shoot at
for n in range(1, 5):
    alien = Alien(5)
    alien.rect.center = (MAXWIDTH / 5 * n, 50)
    aliens.add(alien)
allsprites.add(aliens)


#handle firing the bullets
def fire():
    bullet = dude.shoot()
    bullets.add(bullet)


#check if any aliens are hit by a bullet, and return the earned points
def checkBullets():
    bullethits = pygame.sprite.groupcollide(bullets, aliens, True, False)
    points = 0
    if bullethits:
        for bullet, hits in bullethits.items():
            for alien in hits:
                alien.hitpoints -= bullet.damage
                if alien.hitpoints <= 0:
                    points += alien.points
                    alien.kill()
    return points


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

    #update the sprites & bullets
    bullets.update()
    allsprites.update()

    #check for bullet collisions and update points
    points = checkBullets()
    if points:
        SCORE += points
        print 'score: ', SCORE

    #draw everything on the screen
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    bullets.draw(screen)
    pygame.display.flip()
