from time import time

from INDIGO.objects.engineobject import EngineObject
from pygame.mouse import get_pressed, get_pos


class ButtonMeta(EngineObject):
    last_click = time()

    def check_click(self):
        # check if the button is being click
        mouse = get_pos()
        click = get_pressed()
        x, y, w, h = self.rect
        return x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1

    def blit(self):
        self.blit_func()
        # implement click delay to prevent instant clicks
        if self.check_click() and time() - self.last_click >= self.delay_time:
            self.last_click = time()
            self.resp()
        return
