from INDIGO.objects.engineobject import EngineObject
from pygame.draw import polygon


class Polygon(EngineObject):
    def __init__(self, scr, color, *points):
        """
        Screen scr - the screen object
        tup color - the color of the polygon
        args points - the lists of points as a generator object
        """
        self.scr = scr
        self.color = color
        self.points = list(points)
        return

    def blit(self):
        polygon(self.scr.display, self.color, self.points)
        return

    def __repr__(self):
        module = self.__class__.__module__
        class_name = self.__class__.__name__
        memory_location = hex(id(self))
        return f"<{module}.{class_name} object at {memory_location}>"

    def __str__(self):
        return f"Polygon {repr(self)} composed of lines {self.lines}"
