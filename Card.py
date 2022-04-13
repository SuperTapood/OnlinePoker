# clubs, diamonds, hearts, spades
# 0,     1,        2,      3
import pygame

from Engine import Screen

conv_value = {
    1: "ace",
    11: "jack",
    12: "queen",
    13: "king"
}

conv_type = ["clubs", "diamonds", "hearts", "spades"]


def get_image(value, cls):
    if value in conv_value.keys():
        value = conv_value.get(value)
    cls = conv_type[cls]
    return pygame.image.load(f"Cards\\{value}_of_{cls}.png")


class Card:
    def __init__(self, value, cls):
        self.img = get_image(value, cls)
        if value in conv_value.keys():
            value = conv_value.get(value)[0].upper()
        self.code = f"{value}{conv_type[cls][0]}"
        print(self.code)
        return

    def blit(self):
        Screen.scr.blit(self.img, (0, 0))
    pass
