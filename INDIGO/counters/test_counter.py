from time import time

import numpy as np


# test spf and fps counter

class TestCounter:
    def __init__(self):
        # ndarrays are like the lists bigger, better, cooler brother
        # and numpy is generally pretty cool
        self.times = np.array([])
        self.time = None
        return

    def start(self):
        # reset the time
        self.time = time()
        return

    def lap(self):
        # add the elapsed time to the times ndarray
        self.times = np.append(self.times, time() - self.time)
        return

    def __str__(self):
        # print out le results
        mean = np.mean(self.times)
        return f"{mean} SPF\n {1 / mean} FPS"

    pass
