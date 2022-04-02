# a cute little fps counter

from time import time


class Counter:
    def __init__(self):
        self.start_time = 0
        return

    def start(self):
        # reset the clock
        self.start_time = time()
        return

    def lap(self):
        # print the fps count = 1 / time elapsed
        end_time = time() - self.start_time
        try:
            print(f"FPS - {1 / end_time}")
        except ZeroDivisionError:
            # sometimes end_time will just round to 0 and
            # dividing by 0 is not cool bruh
            print(f"FPS cannot be measured")
        return

    pass
