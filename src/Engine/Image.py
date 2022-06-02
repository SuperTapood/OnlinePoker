import pygame
from .Screen import Screen


class Image:
    def __init__(self, path, x, y):
        """
        create a new image
        :param path: the path to the image
        :param x: the x position of the image
        :param y: the y position of the image
        """
        self.img = pygame.image.load(path)
        self.x = x
        self.y = y
        return

    def blit(self):
        """
        draw the image on screen
        """
        Screen.get().blit(self.img, (self.x, self.y))
        return
    pass
