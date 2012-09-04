#!/usr/bin/python
from helpers import *
import pygame
from Bullet import Bullet
from pygame.locals import *


class Alien(pygame.sprite.DirtySprite):
    def __init__(self, points):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = load_image('alien.bmp')
        self.moving = False
        self.hitpoints = 2
        self.points = points
        self.vector = (0, 0)

    def update(self):
        self.dirty = 1
        self.rect.move_ip(self.vector)
