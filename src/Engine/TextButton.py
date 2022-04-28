from .Button import Button
from .Text import Text as Label
from .Colors import *


class TextButton:
    def __init__(self, txt, x, y, txt_size=35, txt_color=white, resp=lambda: None, button_width=0):
        """
        str txt - the text to blitted on screen
        num x, y - the loc of the button
        int txt_size - the size of the text
        tup txt_color, button_color - the colors of the text and the button
        func resp - the response to a click
        num border_width - the border's width
        """
        self.att_tuple = (x, y, txt_size, txt_color, resp)
        rect = Label(txt, x, y, txt_color=txt_color, font_size=txt_size).rect
        x, y, w, h = rect
        self.pos = (x, y)
        self.button = Button(x, y, w, h)
        self.text = Label(txt, x, y, txt_color=txt_color, font_size=txt_size)
        self.resp = resp
        return

    def blit(self):
        self.text.blit()
        if self.button.check_click():
            self.resp()
        return

    def update_text(self, new_txt):
        x, y, txt_size, txt_color, resp = self.att_tuple
        rect = Label(new_txt, x, y, txt_size, txt_color).rect
        x, y, w, h = rect
        self.button = Button(x, y, w, h, )
        self.text = Label(new_txt, x, y, txt_size, txt_color)
        return

    pass
