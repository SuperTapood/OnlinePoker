from Deck import Deck
from Evaluator import Evaluator as Eval


class Hand:
    def __init__(self):
        self.cards = [Deck.deal() for _ in range(7)]
        self.codes = list([c.code for c in self.cards])
        return

    def eval(self):
        rank1 = Eval.evaluate_cards(["9c", "4c", "4s", "9d", "4h", "Qc", "6c"])
        rank2 = Eval.evaluate_cards(["9c", "4c", "4s", "9d", "4h", "2c", "9h"])
        print(rank1)
        print(rank2)
    pass
