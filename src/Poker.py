import copy
import random
import pygame
from _socket import SHUT_RDWR

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
from time import time


class Poker:
    scr = None
    # funny haha lol
    quotes = [
        "*sigh* i guess you are my little pugchamp",
        "made with <3",
        "where are my pants?",
        "*Texas Hold 'em",
        "Spain but the S is silent",
        "putting the fun in dysfunctional",
        "now with 5% more Bob Ross",
        "I hardly know 'er!",
        "more cheese = less cheese",
        "How you BEAN?",
        "You're breathtaking!",
        "you egg?",
        "The embodiment of page 2 of google search results",
        "Love is like frying food shirtless, you never know when it's going to hurt",
        "Water is just hydrogen soup",
        "Hey, got any grapes?",
        "What does a cloud wear under his pants? Thunderwear.",
        "Paper puns are just tearable",
        "Need an ark? I Noah guy",
        "I don't get why circles exist. They're pointless.",
        "I'm afraid for the calendar. Its days are numbered.",
        "What has ears but can't listen? Corn.",
        "If the USA is so great why did they make a USB?",
        "Why are ducks always in a fowl mood?",
        f"it is {calendar.day_name[date.today().weekday()]} my dudes",
        "Approved by official code chads",
        "If it compiles, it's good; if it boots up, it's perfect.",
        "It Just Works.",
        "I love it when asynchronization works 80% out of 5% of the time",
        "The numbers Mason! What do they mean?!?!",
        "funny quote go brrrrr",
        "Built by two part time idiot sandwiches"
    ]

    t_quotes = copy.copy(quotes)

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
        self.pot_text = Text(f"Pot contains {self.pot}", 1000, 800, font_size=50)
        self.server_logic_run = True
        self.loop_thread_run = True
        self.readables = []
        return

    def get_quote(self):
        """
        get a random quote
        :return: a random quote
        """
        if len(self.t_quotes) == 0:
            self.t_quotes = copy.copy(self.quotes)
        return self.t_quotes.pop(random.randint(0, len(self.t_quotes) - 1))

    def quit(self):
        """
        terminate this instance of the game
        """
        pygame.quit()
        self.server_logic_run = False
        self.loop_thread_run = False
        return

    def start_screen(self):
        """
        boot the start screen and load the game's cards
        """
        loading_thread = threading.Thread(target=self.load_deck)
        loading_thread.start()
        y = 400
        height = 150
        loading_text = Text("loading game assets...", self.width - 350, 250)
        funny = Text(self.get_quote(), 0, y + 35, font_size=50)
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
        self.cont = TextButton("START", 750, 650, txt_size=60, resp=self.set_b_to_true)
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

    # set b to true
    def set_b_to_true(self):
        """
        set b to true
        """
        # set b to true
        self.b = True  # set b to true
        # b is now true
        return  # b has been set to true

    def load_deck(self):
        """
        thread function for the loading of the cards
        """
        for i in range(1, 14):
            for j in range(4):
                card = Card(i, j)
                # append the card to both lists, this makes loading so much faster
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
        """
        the main menu loop function
        """
        last = time()
        delay = 0.3
        title = Text("Poker", 0, 0, font_size=150)
        title.rect.center = (1700 / 2, 60)
        quote = TextButton(self.get_quote(), 50, 750, txt_size=30)
        quote.text.rect.center = (1700 / 2, 160)
        quote.button.rect = quote.text.rect
        create = TextButton("Create a New Match", 0, 0, resp=self.create_match, txt_size=70)
        create.text.rect.center = (1700 / 2, 330)
        create.button.rect = create.text.rect
        join = TextButton("Join an Existing Match", 0, 0, resp=self.join_match, txt_size=70)
        join.text.rect.center = (1700 / 2, 500)
        join.button.rect = join.text.rect
        quit_button = TextButton("Quit", 0, 0, resp=self.quit, txt_size=70)
        quit_button.text.rect.center = (1700 / 2, 870)
        quit_button.button.rect = quit_button.text.rect

        while not self.b:
            Screen.scr.fill(black)
            title.blit()
            create.blit()
            quote.blit()
            join.blit()
            quit_button.blit()
            if quote.button.check_click() and time() - last > delay:
                last = time()
                quote.text.set_text(self.get_quote())
                quote.text.rect.center = (1700 / 2, 160)
                quote.button.rect = quote.text.rect
            if not self.handle_events():
                self.quit()
            pygame.display.update()

        return

    def create_match(self):
        """
        create a new match by opening the socket for incoming requests
        """
        self.hands = [Hand(i) for i in range(7)]
        for h in self.hands:
            h.compute_codes(self.hands)
        self.b = True

        # ip = socket.gethostbyname(socket.gethostname())
        ip = "127.0.0.1"

        addr = Text("your ip is " + ip, 50, 50)

        self.socket.bind((ip, 42069))
        self.socket.listen(500)
        cash_value = 10000

        # settings loop goes here

        self.cash_values = [cash_value] * 4
        self.cashes = [Text(f"Player {i + 1}: {self.cash_values[i]}", 1000, i * 150, font_size=50) for i in range(4)]

        self.server_logic.start()
        return

    def game_full(self):
        """
        called when the requested game is full
        """
        text = Text("The game you wanted to join is full", 50, 50)
        self.b = True

        while self.b:
            Screen.scr.fill(black)
            text.blit()
            if not self.handle_events():
                self.quit()
            pygame.display.update()

        return

    def join_match(self):
        """
        join an existing match
        """
        self.b = True
        if not self.is_connected:
            self.socket.connect(("127.0.0.1", 42069))
            self.is_connected = True
            d = recv_msg(self.socket)
            if d == "connection refused":
                # game is full
                self.socket.close()
                self.game_full()
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
            for i, hand in zip(range(len(self.hands)), self.hands):
                hand.set_index(i)
            for h in self.hands:
                h.compute_codes(self.hands)
            cash_value = int(recv_msg(self.socket))
            self.cash_values = [cash_value] * 4
            self.cashes = [Text(f"Player {i + 1}: {self.cash_values[i]}", 1000, i * 150, font_size=50) for i in
                           range(4)]
        return

    def server_process(self, data):
        pass

    def first_connect(self, sockt):
        """
        connect the given socket to our socket by quickly bringing it up to speed
        :param sockt: the given socket
        """
        self.connected += 1
        send_msg(sockt, b"connection accepted")
        send_msg(sockt, self.connected)
        for hand in self.hands:
            # print(str(hand))
            send_msg(sockt, str(hand).encode())
        send_msg(sockt, f"{self.cash_values[0]}")
        return

    def server_logic_thread(self):
        """
        function to handle all of the game managing and stuff. this loop coexists with the main loop to prevent the
        sockets from blocking the render loop
        """
        self.readables = [self.socket]
        while self.loop_thread_run:
            read, _, _ = select(self.readables, [], [])
            for sock in read:
                if self.loop_thread_run:
                    if sock is self.socket:
                        sockt, addr = sock.accept()
                        if self.connected < 1:
                            self.readables.append(sockt)
                            self.first_connect(sockt)
                            print("connected to", addr)
                        else:
                            send_msg(sockt, b"connection refused")
                            sockt.close()
                            print("kicked", addr)
                    else:
                        d = sock.recv(2048)
                        if d:
                            self.server_process(d)
                        else:
                            self.readables.remove(sock)
                            sock.close()

    def game_loop(self):
        pass

    def blit(self):
        """
        draw all elements of the game
        """
        for h in self.hands:
            h.blit()
        self.scr.line(white, (1000, 0), (1000, 1000), 5)
        self.scr.rect(black, 1000, 0, 1000, 1000)
        for c in self.cashes:
            c.blit()
        self.pot_text.blit()
        return

    pass
