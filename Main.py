import random
import sys
import pygame

from Card import Card
from Deck import Deck
from Engine import *
from Hand import Hand
import threading


class Poker:
    scr = None
    quotes = [
        "this is poggers lol",
        "you wot mate",
        "*sigh* i guess you are my little pugchamp",
        "made with <3",
        "where are my pants?",
        "*Texas Hold 'em",
        "Spain but the S is silent",
        "putting the fun in dysfunctional",
        "now with 5% more Bob Ross",
        "I hardly know 'er!",
        "more cheese = less cheese",
        "how you BEAN?"
    ]

    def __init__(self):
        """
        create a new instance of the game
        """
        self.clock = pygame.time.Clock()
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
        funny = Text(self.quotes[random.randint(0, len(self.quotes) - 1)], 0, y)
        funny.rect.x -= funny.rect.width * 2
        percent = Text("0.69% done", 0, 250)
        while self.__card_counter < 52:
            self.clock.tick(60)
            self.scr.scr.fill(black)
            percent.set_text(f"{int((self.__card_counter / 52) * 100)}% done")
            percent.blit()
            funny.rect.x = 800 - 800 * (self.__card_counter / 52)
            loading_text.blit()
            pygame.draw.rect(self.scr.scr, dark_red, pygame.Rect(800 - width * (self.__card_counter / 52), y, 800, height))
            funny.blit()
            pygame.display.update()
            if not self.handle_events():
                pygame.quit()
                sys.exit()
        percent.set_text("100% done")
        self.b = False
        self.cont = TextButton("START", 250, 600, txt_size=60, resp=self.contin)
        while not self.b:
            self.cont.blit()
            pygame.display.update()
            if not self.handle_events():
                pygame.quit()
                sys.exit()
        loading_thread.join()
        return

    def contin(self):
        self.b = True
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
        game = Poker()
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
