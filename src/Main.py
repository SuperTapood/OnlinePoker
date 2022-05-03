import random
import sys
import pygame

from Card import Card
from Deck import Deck
from Engine import *
from Hand import Hand
import threading
import socket
from select import select


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
        self.width = 1000
        self.height = 1000
        self.clock = pygame.time.Clock()
        self.scr = Screen(self.width, self.height)
        self.__card_counter = 0
        self.deck = Deck()
        self.socket = socket.socket()
        self.logic = threading.Thread(target=self.logic_thread)
        self.connected = 0
        loading_thread = threading.Thread(target=self.load_deck)
        loading_thread.start()
        y = 400
        height = 150
        loading_text = Text("loading game assets...", self.width - 350, 250)
        funny = Text(self.quotes[random.randint(0, len(self.quotes) - 1)], 0, y, font_size=50)
        funny.rect.x -= funny.rect.width * 2
        percent = Text("0.69% done", 0, 250)
        while self.__card_counter < 52:
            self.clock.tick(60)
            self.scr.scr.fill(black)
            percent.set_text(f"{int((self.__card_counter / 52) * 100)}% done")
            percent.blit()
            funny.rect.x = self.width - self.width * (self.__card_counter / 52)
            loading_text.blit()
            pygame.draw.rect(self.scr.scr, dark_red,
                             pygame.Rect(self.width - self.width * (self.__card_counter / 52), y,
                                         self.width + 200, height))
            funny.blit()
            pygame.display.update()
            if not self.handle_events():
                pygame.quit()
                sys.exit()
        percent.set_text("100% done")
        self.b = False
        self.cont = TextButton("START", 500, 600, txt_size=60, resp=self.contin)
        while not self.b:
            self.scr.scr.fill(black)
            percent.blit()
            pygame.draw.rect(self.scr.scr, dark_red,
                             pygame.Rect(self.width - self.width * (self.__card_counter / 52), y,
                                         self.width + 200, height))
            self.cont.blit()
            funny.blit()
            pygame.display.update()
            if not self.handle_events():
                pygame.quit()
                sys.exit()
        loading_thread.join()
        self.hands = [Hand(i) for i in range(7)]
        self.b = False
        self.is_connected = False
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
        create = TextButton("create match", 50, 50, resp=self.create_match)
        join = TextButton("join match", 250, 50, resp=self.join_match)

        while not self.b:
            Screen.scr.fill(black)
            create.blit()
            join.blit()
            if not self.handle_events():
                pygame.quit()
                sys.exit()
            pygame.display.update()

    def create_match(self):
        self.b = True

        # socket.gethostbyname(socket.gethostname())

        addr = Text("your ip is " + "127.0.0.1", 50, 50)

        self.socket.bind(("127.0.0.1", 42069))
        self.socket.listen(3)

        self.logic.start()
        while True:
            Screen.scr.fill(black)
            addr.blit()
            if not self.handle_events():
                pygame.quit()
                sys.exit()
            pygame.display.update()

    def join_match(self):
        if not self.is_connected:
            self.socket.connect(("127.0.0.1", 42069))
            self.is_connected = True
            d = self.socket.recv(4096)
            if d == b"connection refused":
                # game is full
                self.socket.close()
                pygame.quit()
                sys.exit()
        return

    def process(self, data):
        pass

    def logic_thread(self):
        readables = [self.socket]
        while True:
            read, _, _ = select(readables, [], [])

            for sock in read:
                if sock is self.socket:
                    sockt, addr = sock.accept()
                    if self.connected < 3:
                        readables.append(sockt)
                        self.connected += 1
                        sockt.sendall(b"connection accepted")
                        # print("connected to", addr)
                    else:
                        sockt.sendall(b"connection refused")
                        readables.remove(sock)
                        sock.close()
                        sockt.close()
                else:
                    d = sock.recv(2048)
                    if d:
                        self.process(d)
                    else:
                        readables.remove(sock)
                        sock.close()

    pass


if __name__ == "__main__":
    try:
        pygame.init()
        game = Poker()
        # todo: do this after finishing the game dummy
        game.main_menu()
        # todo: fix the eval thing and add the community cards
        # for h in hands:
        #     print(h.eval())
        # todo: fix the image rotation thing to copy rather than override
        # todo: crash a client that cannot connect
        # todo: add a client logic thread and server logic thread
        while True:
            game.clock.tick(60)
            Screen.scr.fill(black)
            for h in game.hands:
                h.blit()
            pygame.display.update()
            if not game.handle_events():
                pygame.quit()
                sys.exit()
    except pygame.error as _:
        print(_)
