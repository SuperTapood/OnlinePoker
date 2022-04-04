import threading
from INDIGO.colors import *
import pygame
from time import sleep
from INDIGO import *


class Poker:
    def __init__(self):
        self.scr = Screen(800, 800, BLACK)
        self.card = load_file("Cards//ace_of_clubs.png", 50, 50)
        return

    # render thread
    def render(self):
        self.card.blit(self.scr)
        return

    pass


if __name__ == "__main__":
    game = Poker()
    # create render and network threads
    render_thread = threading.Thread(target=game.render)
    render_thread.start()
    while True:
        game.scr.update()
