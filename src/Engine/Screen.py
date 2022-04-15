import pygame


class Screen:
    scr: pygame.Surface
    x: int
    y: int

    def __new__(cls, x, y):
        Screen.scr = pygame.display.set_mode((x, y))
        Screen.x = x
        Screen.y = y
        return cls

    @staticmethod
    def get() -> pygame.Surface:
        return Screen.scr

    @staticmethod
    def line(color, start, end, width):
        pygame.draw.line(Screen.get(), color, start, end, width)
    pass
