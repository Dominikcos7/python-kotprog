from enum import Enum


class Rank(Enum):
    ACE = "ace"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"
    SIX = "six"
    SEVEN = "seven"
    EIGHT = "eight"
    NINE = "nine"
    TEN = "ten"
    JACK = "jack"
    QUEEN = "queen"
    KING = "king"

    def __str__(self):
        return "%s" % self.value

    def as_treys_rank(self) -> str:
        match self:
            case self.TWO:
                return '2'
            case self.THREE:
                return '3'
            case self.FOUR:
                return '4'
            case self.FIVE:
                return '5'
            case self.SIX:
                return '6'
            case self.SEVEN:
                return '7'
            case self.EIGHT:
                return '8'
            case self.NINE:
                return '9'
            case self.TEN:
                return 'T'
            case self.JACK:
                return 'J'
            case self.QUEEN:
                return 'Q'
            case self.KING:
                return 'K'
            case self.ACE:
                return 'A'
