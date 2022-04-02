from INDIGO.objects.engine_object import EngineObject

from INDIGO.objects.buttons.text_button import Text_Button


class InputField(EngineObject):
    def __init__(self, scr, x, y, txt_size, txt_color, button_color, max_len, delay_time=0.3):
        """
        Screen scr - the screen object
        num x, y - the loc of the input field
        int txt_size - the size of the text
        tup txt_color - the color of the button
        tup button_color - the color of the button
        int max_len - the max length of the text
        """
        self.max_len = max_len
        self.txt = ""
        self.active = False
        self.button = Text_Button(scr, self.get_text(), x, y, txt_size, txt_color, button_color,
                                  self.change_active_state, delay_time)
        return

    def get_text(self):
        # get the text and modify it for the text button
        if len(self.txt) == self.max_len:
            return self.txt
        elif len(self.txt) > self.max_len:
            return self.txt[:self.max_len]
        else:
            return self.txt + " " * (self.max_len - len(self.txt))

    def blit(self):
        self.button.blit()
        return

    def change_active_state(self):
        self.active = not self.active
        return

    def update_text(self, txt):
        if self.active:
            self.txt += txt
            self.button.update_text(self.get_text())
        return
