#!/usr/bin/python
from helpers import *
import pygame
from pygame.locals import *

class Dude(pygame.sprite.DirtySprite):

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = load_image('dude.bmp')

    def update(self):
        self.dirty = 1