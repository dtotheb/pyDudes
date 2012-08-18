#!/usr/bin/python
from helpers import *
import pygame
from pygame.locals import *


class Dude(pygame.sprite.DirtySprite):

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = load_image('dude.bmp')
        self.moving = False

    #handles moving the dude
    def move(self, speed):
        if self.moving == 'right':
            self.rect.move_ip(speed, 0)
        if self.moving == 'left':
            self.rect.move_ip(-speed, 0)
        if self.moving == 'up':
            self.rect.move_ip(0, -speed)
        if self.moving == 'down':
            self.rect.move_ip(0, speed)

    def update(self):
        self.dirty = 1
        self.move(5)
