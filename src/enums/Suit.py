from enum import Enum


class Suit(Enum):
    SPADE = "spade",
    HEART = "heart",
    DIAMOND = "diamond",
    CLUB = "club",

    def __str__(self):
        return "%s" % self.value
    
