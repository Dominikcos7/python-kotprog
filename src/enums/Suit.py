from enum import Enum


class Suit(Enum):
    """
    Represents the suit (colour) of a card in poker.
    """

    SPADE = "spade",
    HEART = "heart",
    DIAMOND = "diamond",
    CLUB = "club",

    def __str__(self):
        return "%s" % self.value

    def as_treys_suit(self) -> str:
        """
        Returns the suit in a format that Treys library can use.
        """
        match self:
            case self.SPADE:
                return 's'
            case self.HEART:
                return 'h'
            case self.CLUB:
                return 'c'
            case self.DIAMOND:
                return 'd'
