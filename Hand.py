from Deck import Deck
from Evaluator import Evaluator


class Hand:
    def __init__(self):
        self.cards = [Deck.deal() for _ in range(7)]
        self.codes = list([c.code for c in self.cards])
        return

    def eval(self):
        return Evaluator.evaluate_cards()
    pass
