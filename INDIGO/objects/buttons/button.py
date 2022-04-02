from pygame.draw import rect

from INDIGO.objects.buttons.button_meta import ButtonMeta


class Button(ButtonMeta):
    def __init__(self, scr, x, y, w, h, color, resp=lambda: None, border_width=0, click_delay=0.3):
        """
        Screen scr - the screen to be blitted on
        num x, y, w, h - the dims and locs of the button
        tup color - the color of the button
        func resp - the response to the click
        num border_width - the width of the border of the button
        """
        self.resp = resp
        self.display = scr
        self.rect = (x, y, w, h)
        self.color = color
        self.border_width = border_width
        self.delay_time = click_delay
        return

    def blit_func(self):
        rect(self.display, self.color, self.rect, self.border_width)
        return

    pass
