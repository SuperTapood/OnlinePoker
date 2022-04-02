from INDIGO.objects.engineobject import EngineObject
from pygame.draw import line


class Line(EngineObject):
    def __init__(self, start_x, start_y, end_x, end_y, width, color, scr):
        """
        num start_x, start_y, end_x, end_y - the locs of the two dots
        num width - the width of the line
        tup color - the color of the line
        Screen scr - the screen object
        """
        self.x1 = start_x
        self.x2 = end_x
        self.y1 = start_y
        self.y2 = end_y
        self.color = color
        self.width = width
        self.display = scr
        return

    def __repr__(self):
        module = self.__class__.__module__
        class_name = self.__class__.__name__
        memory_location = hex(id(self))
        return f"<{module}.{class_name} object at {memory_location}>"

    def __str__(self):
        return f"Line {repr(self)} from ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})"

    def blit(self):
        line(self.display, self.color, (self.x1, self.y1), (self.x2, self.y2), self.width)
        return
