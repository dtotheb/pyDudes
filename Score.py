from helpers import *
import pygame


class Score(pygame.sprite.Sprite):
    """A sprite for the score."""

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.font = pygame.font.Font(None, 50)

        self.score = 0
        self.reRender()

    def update(self):
        self.reRender()

    """Updates the score. Renders a new image
     and re-centers at the initial coordinates."""
    def reRender(self):
        self.image = self.font.render("Score: %d"%(self.score), True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
