import sys
import pygame

from Deck import Deck
from Engine import *
from Hand import Hand


class Chess:
    scr = None

    def __init__(self):
        """
        create a new instance of the game
        """
        self.scr = Screen(800, 800)
        self.deck = Deck()
        self.index = 0
        self.clock = pygame.time.Clock()
        return

    @staticmethod
    def handle_events():
        """
        handle pygame events
        :return: false if the game is being closed, else true
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def main_menu(self):
        return

    def create_match(self):
        return

    def join_match(self):
        return
    pass


if __name__ == "__main__":
    try:
        pygame.init()
        game = Chess()
        # todo: do this after finishing the game dummy
        # game.main_menu()
        hands = [Hand(i) for i in range(2)]
        while True:
            game.clock.tick(60)
            Screen.scr.fill(black)
            for h in hands:
                h.blit()
            pygame.display.update()
            if not game.handle_events():
                pygame.quit()
                sys.exit()
    except pygame.error as _:
        print(_)
