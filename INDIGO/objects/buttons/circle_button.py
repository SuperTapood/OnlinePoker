from INDIGO.objects.buttons.button_meta import ButtonMeta
from INDIGO.objects.shapes import Circle


class CircleButton(ButtonMeta):
    def __init__(self, scr, color, x, y, radius, resp=lambda: None, width=0, delay_time=0.3):
        """
        Screen scr - the screen object
        tup color - the color of the circle
        num radius - the radius of the circle
        func resp - the response to click
        num width - the width of the border of the circle
        """
        self.circle = Circle(scr, color, (x, y), radius, width)
        self.x = x
        self.y = y
        self.resp = resp
        # need a special rect for this
        self.rect = x - radius, y - radius, radius * 2, radius * 2
        self.delay_time = delay_time
        return

    def blit_func(self):
        self.circle.blit()
        return
