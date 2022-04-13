from Engine import *


class Pawn:
    def __init__(self, index, is_black=False):
        name = "White" if not is_black else "Black"
        self.img = Image("Pieces/" + name + "Pawn.png", 50, 50)
        return

    def blit(self):
        self.img.blit()
        return

    pass
