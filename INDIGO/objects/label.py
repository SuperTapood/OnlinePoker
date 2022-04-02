import pygame

from INDIGO.objects.engineobject import EngineObject


class Label(EngineObject):
    def __init__(self, scr, txt, x, y, font_size, color, font="freesansbold.ttf"):
        self.scr = scr
        self.txt = txt
        font = pygame.font.Font(font, font_size)
        self.text = font.render(txt, True, color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)
        return

    def blit(self):
        self.scr.blit(self.text, self.rect.x, self.rect.y)
        return

    def __repr__(self):
        module = self.__class__.__module__
        class_name = self.__class__.__name__
        memory_location = hex(id(self))
        return f"<{module}.{class_name} object at {memory_location}>"

    def __str__(self):
        return f"Label {repr(self)} of text {self.text} at loc ({self.rect.x}, {self.rect.y})"
