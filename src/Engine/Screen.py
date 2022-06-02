import pygame


class Screen:
    scr: pygame.Surface
    width: int
    y: int

    def __new__(cls, width, height):
        """
        create a new Screen object. allows me to initialize static objects
        :param width: the width of the screen
        :param height: the height of the screen
        """
        Screen.scr = pygame.display.set_mode((width, height))
        Screen.width = width
        Screen.height = height
        return cls

    @staticmethod
    def get() -> pygame.Surface:
        """
        get the pygame surface representing the screen
        :return: the screen
        """
        return Screen.scr

    @staticmethod
    def line(color, start, end, width):
        """
        draw a line on screen with the given specs
        :param color: the color of the line
        :param start: the start position of the line
        :param end: the end position of the line
        :param width: the width of the line
        """
        pygame.draw.line(Screen.get(), color, start, end, width)
        return
    pass
