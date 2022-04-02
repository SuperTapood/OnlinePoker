from INDIGO.objects.engine_object import EngineObject

from INDIGO.objects.buttons.button import Button
from INDIGO.objects.label import Label


class TextButton(EngineObject):
    def __init__(self, scr, txt, x, y, txt_size, txt_color, button_color, resp=lambda: None, button_width=0):
        """
        Screen scr - the screen object
        str txt - the text to blitted on screen
        num x, y - the loc of the button
        int txt_size - the size of the text
        tup txt_color, button_color - the colors of the text and the button
        func resp - the response to a click
        num border_width - the border's width
        """
        self.att_tuple = (scr, x, y, txt_size, txt_color, button_color, resp, button_width)
        rect = Label(scr, txt, x, y, txt_size, txt_color).get_rekt()
        x, y, w, h = rect
        self.pos = (x, y)
        self.button = Button(scr, x, y, w, h, button_color, resp, button_width)
        self.text = Label(scr, txt, x, y, txt_size, txt_color)
        return

    def blit(self):
        self.button.blit()
        self.text.blit()
        return

    def update_text(self, new_txt):
        scr, x, y, txt_size, txt_color, button_color, resp, button_width = self.att_tuple
        rect = Label(scr, new_txt, x, y, txt_size, txt_color).get_rekt()
        x, y, w, h = rect
        self.button = Button(scr, x, y, w, h, button_color, resp, button_width)
        self.text = Label(scr, new_txt, x, y, txt_size, txt_color)
        return

    def __repr__(self):
        module = self.__class__.__module__
        class_name = self.__class__.__name__
        memory_location = hex(id(self))
        return f"<{module}.{class_name} object at {memory_location}>"

    def __str__(self):
        return f"Text Button of text {self.text.txt} at {self.pos}"
