#!/usr/bin/python
import sys
import pygame
from pygame.locals import *
from helpers import *
from Dude import Dude

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


#run the game loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #check if the ball is clicked on
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()


    allsprites.update()
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()