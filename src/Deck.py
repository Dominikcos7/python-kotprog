from random import shuffle

from src.enums.Rank import Rank
from src.enums.Suit import Suit
from src.Card import Card


class Deck:
    def __init__(self):
        self.cards = []

        for rank in Rank:
            for suit in Suit:
                self.cards.append(Card(suit, rank))

    def draw(self) -> Card:
        if len(self.cards) <= 0:
            raise ValueError("Cannot draw from an empty deck.")

        return self.cards.pop(0)

    def shuffle(self) -> "Deck":
        if len(self.cards) < 52:
            raise ValueError('Incomplete deck cannot be shuffled.')

        shuffle(self.cards)
        return self
