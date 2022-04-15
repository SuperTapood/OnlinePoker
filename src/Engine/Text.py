import pygame
from .Colors import *
from .Screen import *


class Text:
    def __init__(self, txt, x, y, txt_color=white, font_size=35):
        self.x = x
        self.y = y
        self.text_color = txt_color
        self.font_size = font_size
        self.font = pygame.font.Font("segoeui.ttf", font_size)
        self.text = self.font.render(txt, False, txt_color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)
        return

    def blit(self):
        Screen.scr.blit(self.text, (self.rect.x, self.rect.y))
        return

    def set_text(self, text):
        self.font = pygame.font.Font("segoeui.ttf", self.font_size)
        self.text = self.font.render(text, False, self.text_color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (self.x, self.y)
        return

    pass
