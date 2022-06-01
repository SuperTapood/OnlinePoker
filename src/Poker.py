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
from Network import send_msg, recv_msg
from datetime import date
import calendar


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
        "how you BEAN?",
        "You're breathtaking!",
        "you egg?",
        "the embodiment of page 2 of google search results",
        "Love is like frying food shirtless, you never know when it's going to hurt",
        "Water is just hydrogen soup",
        "Got any grapes?",
        "Thunderwear",
        "Paper jokes are just tearable",
        "Need an ark? I noah guy",
        "I don't get why circles exist. They're pointless.",
        "I'm afraid for the calendar. Its days are numbered.",
        "What has ears but can't listen?",
        "If the USA is so great than why did they make a USB",
        "Why are ducks always in a fowl mood",
        f"it's {calendar.day_name[date.today().weekday()]} my dudes"
    ]

    def __init__(self):
        """
        create a new instance of the game and create a bunch of needed variables
        """
        self.b = None
        self.cont = None
        self.width = 1700
        self.height = 1000
        self.clock = pygame.time.Clock()
        self.scr = Screen(self.width, self.height)
        self.__card_counter = 0
        self.deck = Deck()
        self.socket = socket.socket()
        self.server_logic = threading.Thread(target=self.server_logic_thread)
        self.connected = 0
        self.cash_values = []
        self.cashes = []
        self.index = 0
        self.loop_thread = threading.Thread(target=self.game_loop)
        self.hands = []
        self.is_connected = False
        self.pot = 0
        self.pot_text = Text(f"Pot contains {self.pot}", 0, 200, font_size=50)
        self.server_logic_run = True
        self.loop_thread_run = True
        return

    def quit(self):
        pygame.quit()
        self.server_logic_run = False
        self.loop_thread_run = False

    def start_screen(self):
        """
        boot the start screen and load the game's cards
        """
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
                self.quit()
        percent.set_text("100% done")
        self.b = False
        self.cont = TextButton("START", 500, 600, txt_size=60, resp=self.set_b_true)
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
                self.quit()

        loading_thread.join()
        self.b = False
        return

    def set_b_true(self):
        self.b = True
        return

    def load_deck(self):
        for i in range(1, 14):
            for j in range(4):
                card = Card(i, j)
                self.deck.pack.append(card)
                self.deck.backup.append(card)
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
                self.quit()
            pygame.display.update()

    def create_match(self):
        self.hands = [Hand(i) for i in range(7)]
        for h in self.hands:
            h.compute_codes(self.hands)
        self.b = True

        # ip = socket.gethostbyname(socket.gethostname())
        ip = "127.0.0.1"

        addr = Text("your ip is " + ip, 50, 50)

        self.socket.bind((ip, 42069))
        self.socket.listen(3)
        cash_value = 10000

        # settings loop goes here

        self.cash_values = [cash_value] * 4
        self.cashes = [Text(f"Player {i + 1}: {self.cash_values[i]}", 0, i * 50, font_size=50) for i in range(4)]

        self.server_logic.start()

    def join_match(self):
        self.b = True
        if not self.is_connected:
            self.socket.connect(("127.0.0.1", 42069))
            self.is_connected = True
            d = recv_msg(self.socket)
            if d == "connection refused":
                # game is full
                self.quit()
            self.index = int(recv_msg(self.socket))
            for _ in range(7):
                d = recv_msg(self.socket)
                self.hands.append(Hand(_, d))
            for _ in range(self.index):
                temp = self.hands[0]
                self.hands[0] = self.hands[1]
                self.hands[1] = self.hands[2]
                self.hands[2] = self.hands[3]
                self.hands[3] = temp
            # for i, hand in zip(range(len(self.hands)), self.hands):
            #     hand.set_index(i)
            for h in self.hands:
                h.compute_codes(self.hands)
            cash_value = int(recv_msg(self.socket))
            self.cash_values = [cash_value] * 4
            self.cashes = [Text(f"Player {i + 1}: {self.cash_values[i]}", 0, i * 50, font_size=50) for i in range(4)]
        return

    def server_process(self, data):
        pass

    def server_logic_thread(self):
        readables = [self.socket]
        while self.loop_thread_run:
            read, _, _ = select(readables, [], [])
            for sock in read:
                if self.loop_thread_run:
                    if sock is self.socket:
                        sockt, addr = sock.accept()
                        if self.connected < 3:
                            readables.append(sockt)
                            self.connected += 1
                            send_msg(sockt, b"connection accepted")
                            send_msg(sockt, self.connected)
                            for hand in self.hands:
                                # print(str(hand))
                                send_msg(sockt, str(hand).encode())
                            send_msg(sockt, f"{self.cash_values[0]}")
                            print("connected to", addr)
                        else:
                            send_msg(sockt, b"connection refused")
                            readables.remove(sock)
                            sock.close()
                            sockt.close()
                    else:
                        d = sock.recv(2048)
                        if d:
                            self.server_process(d)
                        else:
                            readables.remove(sock)
                            sock.close()

    def game_loop(self):
        pass

    def blit(self):
        for h in self.hands:
            h.blit()
        for c in self.cashes:
            c.blit()
        self.pot_text.blit()
        return

    pass
