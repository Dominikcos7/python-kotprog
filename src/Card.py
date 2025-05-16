from src.enums.Suit import Suit
from src.enums.Rank import Rank
from treys import Card as tCard


class Card:
    """
    This class represents a poker card.
    """

    def __init__(self, suit: Suit, rank: Rank):
        """
        :param suit: the suit (colour) of the card
        :param rank: the rank (value) of the card
        """

        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        return isinstance(other, Card) and self._suit == other._suit and self._rank == other._rank

    def __hash__(self):
        return hash((self._suit, self._rank))

    def __str__(self) -> str:
        return str(self._rank) + " of " + str(self._suit) + "s"

    def as_treys_card(self) -> int:
        """
        This function returns the card in a format the Treys library can use.
        :return: the card in Treys format (which is an integer)
        """

        return tCard.new(self._rank.as_treys_rank() + self._suit.as_treys_suit())

    @property
    def rank(self) -> Rank:
        return self._rank

    @property
    def suit(self) -> Suit:
        return self._suit
