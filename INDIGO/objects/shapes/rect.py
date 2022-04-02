from INDIGO.objects.engineobject import EngineObject
from pygame.draw import rect


class Rect(EngineObject):
    def __init__(self, scr, color, x, y, w, h, width=0):
        """
        Screen scr - the screen object
        tup color - the color of the rect
        x, y, w, h - the dims of the rect
        int width - the width of the rect
        """
        self.scr = scr
        self.color = color
        self.rect = (x, y, w, h)
        self.width = width
        return

    def blit(self):
        rect(self.scr.display, self.color, self.rect, self.width)
        return

    def __repr__(self):
        module = self.__class__.__module__
        class_name = self.__class__.__name__
        memory_location = hex(id(self))
        return f"<{module}.{class_name} object at {memory_location}>"

    def __str__(self):
        return f"Rect {repr(self)} of rect {self.rect}"
