from INDIGO.objects.engineobject import EngineObject
from pygame.draw import circle


class Circle(EngineObject):
    def __init__(self, scr, color, pos, radius, width=0):
        """
        Screen scr - the screen object
        tup color - the color of the circle
        tup pos - the pos of the circle
        num radius - the radius of the circle
        int width - the width of the circle
        """
        self.scr = scr
        self.color = color
        self.pos = pos
        self.r = radius
        self.width = width
        return

    def blit(self):
        circle(self.scr.display, self.color, self.pos, self.r, self.width)
        return

    def __repr__(self):
        module = self.__class__.__module__
        class_name = self.__class__.__name__
        memory_location = hex(id(self))
        return f"<{module}.{class_name} object at {memory_location}>"

    def __str__(self):
        return f"Circle {repr(self)} at {self.pos} of radius {self.r}"
