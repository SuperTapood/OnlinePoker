from pygame.mouse import get_pressed, get_pos


class Button:
    def __init__(self, x, y, w, h):
        self.rect = (x, y, w, h)
        return

    def is_on(self):
        mx, my = get_pos()
        x, y, w, h = self.rect
        return x + w > mx > x and y + h > my > y

    def check_click(self):
        return self.is_on() and get_pressed()[0] == 1

    pass
