from Deck import Deck
from Evaluator import Evaluator


class Hand:
    def __init__(self, index):
        """
        create a new hand
        :param index: the index of the created hand
        """
        self.cards = [Deck.deal(_, index) for _ in range(2)]
        self.codes = list([c.code for c in self.cards])
        return

    def eval(self):
        """
        evaluate this hand
        :return: an integer value representing how good this hand is. smaller is better.
        """
        return Evaluator.evaluate_cards(self.codes)

    def blit(self):
        """
        draw all cards on screen
        """
        for c in self.cards:
            c.blit()
        return

    def set_index(self, index):
        """
        set the index of this hand to something else.
        please do not use this function and pre-plan hand indices

        :param index: the desired index
        """
        for i in range(5):
            self.cards[i].set_index(i, index)
        return
    pass
