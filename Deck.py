import random
from typing import List

from Card import Card


class Deck:
    """
    the pack of all cards in existence
    """
    pack: List[Card]

    def __new__(cls):
        """
        IDK what new does, but it works with a static class and that is all I need to know
        """
        Deck.pack = []
        for i in range(1, 14):
            for j in range(4):
                Deck.pack.append(Card(i, j))
        return cls

    @staticmethod
    def get_pack():
        """
        :return: the pack ig
        """
        return Deck.pack

    @staticmethod
    def deal(card_index, hand_index):
        """
        pop a card from the deck and set its values straight yo
        :param card_index: the index of the card about to be popped
        :param hand_index: the index oft the hand requesting being dealt
        :return: the much desired card
        """
        return Deck.get_pack().pop(random.randint(0, len(Deck.pack) - 1)).set_index(card_index, hand_index)

    pass
