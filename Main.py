import threading
import pygame

from Card import Card
from Deck import Deck
from Engine import *
from Hand import Hand


class Chess:
    scr = None

    def __init__(self):
        self.scr = Screen(800, 800)
        self.deck = Deck()
        self.index = 0
        return

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        return

    def main_menu(self):
        return

    def create_match(self):
        return

    def join_match(self):
        return

    # render thread
    def render(self):
        hand = Hand()
        hand.eval()
        while True:
            Screen.scr.fill(black)
            self.handle_events()

    pass


if __name__ == "__main__":
    pygame.init()
    game = Chess()
    # todo: do this after finishing the game dummy
    # game.main_menu()
    # create render and network threads
    render_thread = threading.Thread(target=game.render)
    render_thread.start()
    while True:
        pygame.display.update()
        game.handle_events()
