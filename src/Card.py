from src.enums.Suit import Suit
from src.enums.Rank import Rank


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        return isinstance(other, Card) and self._suit == other._suit and self._rank == other._rank

    def __hash__(self):
        return hash((self._suit, self._rank))

    def __str__(self) -> str:
        return str(self._rank) + " of " + str(self._suit) + "s"
