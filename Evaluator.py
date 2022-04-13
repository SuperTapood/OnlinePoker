"""
compressed version of Henry Lee's Poker hand evaluation at https://github.com/HenryRLee/PokerHandEvaluator

The library down from a full package to a class and some utility data (almost 7000 lines of it) by removing uneeded
code

seeing as it was only going to be called under specific conditions, it made no sense to keep it as versatile as it was
"""

from typing import List
from EvalUtil import *


class Evaluator:
    @staticmethod
    def to_id(other: str) -> int:
        """
        Convert a string code of a card to an integer id
        Args:
            other (str): The description of the card. e.g. "2c", "Ah". "T" represents 10
        Returns:
            int: the card's ID
        """
        rank, suit = tuple(other)
        return rank_map[rank] * 4 + suit_map[suit]

    @staticmethod
    def hash_quinary(quinary: List[int], num_cards: int) -> int:
        """
        Hash the given list of cards.

        Args:
            quinary (list[int]): the list of the cards.
            num_cards (int): the number of cards.

        Returns:
            int: the hash value
        """
        sum_numb = 0
        length = len(quinary)

        for rank, cnt in enumerate(quinary):
            if cnt:
                sum_numb += DP[cnt][length - rank - 1][num_cards]
                num_cards -= cnt

        return sum_numb

    @staticmethod
    def evaluate_cards(cards: List[str]) -> int:
        """
        Select the best combination of the five cards from given cards and return its rank.

        Args:
            cards(List[str]): List of cards

        Raises:
            ValueError: Unsupported size of the cards

        Returns:
            int: The rank of the given cards with the best five cards. Smaller is stronger.
        """
        cards = list(map(Evaluator.to_id, cards))
        hand_size = 7

        suit_hash = 0
        for card in cards:
            suit_hash += SUITBIT_BY_ID[card]

        flush_suit = SUITS[suit_hash] - 1

        if flush_suit != -1:
            hand_binary = 0

            for card in cards:
                if card % 4 == flush_suit:
                    hand_binary |= BINARIES_BY_ID[card]

            return FLUSH[hand_binary]

        hand_quinary = [0] * 13
        for card in cards:
            hand_quinary[card // 4] += 1

        return NO_FLUSH[Evaluator.hash_quinary(hand_quinary, hand_size)]
