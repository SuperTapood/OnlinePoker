import pygame
from Engine import *
from Poker import Poker
import atexit


def exit_handler():
    # an exit handler to close the open socket so the program will actually terminate
    game.socket.close()


if __name__ == "__main__":
    # this here children is where the fun begins
    atexit.register(exit_handler)
    try:
        pygame.init()
        game = Poker()
        game.start_screen()
        game.main_menu()
        while True:
            game.clock.tick(60)
            Screen.scr.fill(black)
            game.blit()
            pygame.display.update()
            if not game.handle_events():
                game.quit()
                exit_handler()
                break
    except pygame.error as _:
        pass
        # print(_)
