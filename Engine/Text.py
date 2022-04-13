import pygame
from .Colors import *
from .Screen import *


class Text:
    def __init__(self, txt, x, y, txt_color=white, font_size=35):
        self.font = pygame.font.Font("freesansbold.ttf", font_size)
        self.text = self.font.render(txt, True, txt_color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)
        return

    def blit(self):
        Screen.scr.blit(self.text, (self.rect.x, self.rect.y))
        return

    pass
