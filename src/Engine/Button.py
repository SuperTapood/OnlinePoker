from pygame.mouse import get_pressed, get_pos


class Button:
    def __init__(self, x, y, w, h):
        """
        create a new button. a button is a metaclass to handle click checking for other classes.
        :param x: the x position
        :param y: the y position
        :param w: the width of the button
        :param h: the height of the button
        """
        self.rect = (x, y, w, h)
        return

    def is_on(self):
        """
        check if the cursor is on the button
        :return: true if the cursor is on the button, otherwise false
        """
        mx, my = get_pos()
        x, y, w, h = self.rect
        return x + w > mx > x and y + h > my > y

    def check_click(self):
        """
        check if the button is clicked
        :return: true if the cursor is on the button and the left click is pressed, otherwise false
        """
        return self.is_on() and get_pressed()[0] == 1

    pass
