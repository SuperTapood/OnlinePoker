import pygame
from .Screen import Screen


class Image:
    def __init__(self, path, x, y):
        self.img = pygame.image.load(path)
        self.x = x
        self.y = y
        return

    def blit(self):
        Screen.get().blit(self.img, (self.x, self.y))
        return
    pass
