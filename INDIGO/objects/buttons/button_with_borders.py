from INDIGO.objects.engine_object import EngineObject

from INDIGO.exceptions import InvalidBorderButtonError
from INDIGO.objects.buttons.button import Button
from INDIGO.objects.shapes import Rect


class Button_With_Borders(EngineObject):
    def __init__(self, scr, x, y, w, h, color1, color2, size_factor=1, resp=lambda: None, delay_time=0.3):
        """
        Screen scr - the screen object
        num x, y, w1, h1, w2, h2 - the loc and sizes of the two buttons
        tup color1, color2 - the colors of the two buttons
        func resp - the response to the click
        """
        if size_factor < 1:
            raise InvalidBorderButtonError(w, h, w * size_factor, h * size_factor)
        self.rect = Rect(scr, color1, x, y, w, h)
        self.button = Button(scr, x + ((w - w * size_factor) / 2), y + ((h - h * size_factor) / 2), w * size_factor,
                             h * size_factor, color2, resp, delay_time)
        return

    def blit(self):
        self.button.blit()
        self.rect.blit()
        return

    pass
