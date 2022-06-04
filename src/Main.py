import pygame
from Engine import *
from Poker import Poker
import atexit


if __name__ == "__main__":
    # this here children is where the fun begins
    try:
        pygame.init()
        game = Poker()
        atexit.register(game.exit_handler)
        game.start_screen()
        game.main_menu()
        while True:
            game.clock.tick(60)
            Screen.scr.fill(black)
            game.blit()
            pygame.display.update()
            if not game.handle_events():
                game.quit()
                break
    except pygame.error as _:
        pass
        # print(_)
