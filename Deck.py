import random
from typing import List

from Card import Card


class Deck:
    pack: List[Card]

    def __new__(cls):
        Deck.pack = []
        for i in range(1, 14):
            for j in range(4):
                Deck.pack.append(Card(i, j))
        return cls

    @staticmethod
    def get_pack():
        return Deck.pack

    @staticmethod
    def deal(card_index, hand_index):
        return Deck.get_pack().pop(random.randint(0, len(Deck.pack) - 1)).set_index(card_index, hand_index)

    pass
