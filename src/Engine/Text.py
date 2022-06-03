import copy

import pygame
from .Colors import *
from .Screen import *


class Text:
    def __init__(self, txt, x, y, txt_color=white, font_size=35):
        """
        create a new text instance

        :param txt: the text
        :param x: the x position
        :param y: the y position
        :param txt_color: the color of the text
        :param font_size: the font size to use
        """
        self.x = x
        self.y = y
        self.txt = txt
        self.text_color = txt_color
        self.font_size = font_size
        self.font = pygame.font.Font("segoeui.ttf", font_size)
        self.text = self.font.render(txt, False, txt_color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)
        return

    def blit(self):
        """
        draw the text
        """
        Screen.scr.blit(self.text, (self.rect.x, self.rect.y))
        return

    def set_text(self, text):
        """
        set the text
        :param text: the new text
        """
        self.font = pygame.font.Font("segoeui.ttf", self.font_size)
        self.text = self.font.render(text, False, self.text_color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (self.x, self.y)
        return

    def get_resized(self, new_size):
        out = copy.copy(self)
        out.font = pygame.font.Font("segoeui.ttf", new_size)
        out.text = out.font.render(self.txt, False, self.text_color)
        return out

    pass
