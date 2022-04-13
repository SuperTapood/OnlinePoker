import pygame
from Engine import *
from Pecs import *

class Board:
    def __init__(self):
        self.parts = []
        self.parts.append(Pawn(0))

    def blit(self):
        for k in range(9):
            Screen.line(white, (k * int(600 / 8) + 100, 100), (k * int(600 / 8) + 100, 700), 2)
            Screen.line(white, (100, k * int(600 / 8) + 100), (700, k * int(600 / 8) + 100), 2)
        for p in self.parts:
            p.blit()
        return
    pass
