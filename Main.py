import threading
import pygame

from Board import Board
from Engine import *


class Poker:
    scr = None

    def __init__(self):
        self.scr = Screen(800, 800)
        self.board = Board()
        return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def main_menu(self):
        title = Text("O n l i n e  C h e s s", 50, 50)
        start = TextButton("create match", 100, 100, 25, resp=lambda: print("hello"))
        while True:
            title.blit()
            start.blit()
            pygame.display.update()
            self.handle_events()
        pass

    # render thread
    def render(self):
        self.handle_events()
        self.board.blit()
        pygame.display.flip()
        pygame.display.update()
        return

    pass


if __name__ == "__main__":
    pygame.init()
    game = Poker()
    game.main_menu()
    # create render and network threads
    render_thread = threading.Thread(target=game.render)
    render_thread.start()
    while True:
        Screen.scr.blit(pygame.transform.flip(Screen.scr, False, True), (0, 0))
