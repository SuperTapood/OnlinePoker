import sys
import pygame

from Card import Card
from Deck import Deck
from Engine import *
from Hand import Hand
import threading


class Chess:
    scr = None

    def __init__(self):
        """
        create a new instance of the game
        """
        self.scr = Screen(800, 800)
        self.__card_counter = 0
        self.deck = Deck()
        loading_thread = threading.Thread(target=self.load_deck)
        loading_thread.start()
        x = 0
        y = 350
        width = 800
        height = 70
        loading_text = Text("loading game assets...", 450, 250)
        while self.__card_counter < 52:
            loading_text.blit()
            pygame.draw.rect(self.scr.scr, dark_red, pygame.Rect(x, y, width * (self.__card_counter / 52), height))
            pygame.display.update()
            self.handle_events()
        loading_thread.join()
        self.clock = pygame.time.Clock()
        return

    def load_deck(self):
        for i in range(1, 14):
            for j in range(4):
                self.deck.pack.append(Card(i, j))
                self.__card_counter += 1
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
