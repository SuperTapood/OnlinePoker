from Deck import Deck
from Evaluator import Evaluator


class Hand:
    def __init__(self, index):
        self.cards = [Deck.deal(_, index) for _ in range(5)]
        self.codes = list([c.code for c in self.cards])
        return

    def eval(self):
        return Evaluator.evaluate_cards(self.codes)

    def blit(self):
        for c in self.cards:
            c.blit()
        return

    def set_index(self, index):
        for i in range(5):
            self.cards[i].set_index(i, index)
    pass
