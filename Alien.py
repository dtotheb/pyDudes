#!/usr/bin/python
from helpers import *
import pygame
from Bullet import Bullet
from pygame.locals import *


class Alien(pygame.sprite.DirtySprite):
    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = load_image('alien.bmp')
        self.moving = False

    def update(self):
        self.dirty = 1
