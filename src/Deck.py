from random import shuffle

from src.enums.Rank import Rank
from src.enums.Suit import Suit
from src.Card import Card


class Deck:
    """
    This class represents a deck of cards.
    """

    def __init__(self):
        self.cards = []

        for rank in Rank:
            for suit in Suit:
                self.cards.append(Card(suit, rank))

    def draw(self) -> Card:
        """
        Draws a card from the deck.
        :return: the card drawn
        :raises ValueError: if the deck is empty
        """

        if len(self.cards) <= 0:
            raise ValueError("Cannot draw from an empty deck.")

        return self.cards.pop(0)

    def shuffle(self) -> "Deck":
        """
        Shuffles the deck randomly.
        :return: the shuffled deck (itself)
        :raises ValueError: if the deck is incomplete (there are cards missing from it)
        """

        if len(self.cards) < 52:
            raise ValueError('Incomplete deck cannot be shuffled.')

        shuffle(self.cards)
        return self
