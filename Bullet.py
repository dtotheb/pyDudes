#!/usr/bin/python
from helpers import *
import pygame
from pygame.locals import *


class Bullet(pygame.sprite.DirtySprite):

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = load_image('bullet.bmp')
        self.speed = 0
        self.damage = 1

    def move(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.y <= 0:
            self.kill()

    def update(self):
        self.dirty = 1
        self.move()
