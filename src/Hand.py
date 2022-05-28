from typing import List

from Deck import Deck
from Evaluator import Evaluator


class Hand:
    def __init__(self, index, names=""):
        """
        create a new hand
        :param index: the index of the created hand
        """
        self.codes = []
        if names != "":
            s = names.split("|")
            self.cards = [Deck.get(s[i], i, index) for i in range(len(s))]
            self.compute_codes()
            return
        if index < 4:
            self.cards = [Deck.deal(_, index) for _ in range(2)]
        elif index == 4:
            self.cards = [Deck.deal(_, index) for _ in range(3)]
        elif index == 5:
            self.cards = [Deck.deal(0, index)]
        elif index == 6:
            self.cards = [Deck.deal(0, index)]
        return

    def compute_codes(self, hands):
        self.codes = list([c.code for c in self.cards])
        self.codes.append(hands[4].cards[0].code)
        self.codes.append(hands[4].cards[1].code)
        self.codes.append(hands[4].cards[2].code)
        self.codes.append(hands[5].cards[0].code)
        self.codes.append(hands[6].cards[0].code)
        return

    def eval(self):
        """
        evaluate this hand
        :return: an integer value representing how good this hand is. smaller is better.
        """
        if self.codes is None:
            raise RuntimeError("heh")
        print("Adwaoipdaplwid")
        print(self.codes)
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
        for i in range(len(self.cards)):
            self.cards[i].set_index(i, index)
        return

    def __str__(self):
        return "|".join(self.codes)

    pass
