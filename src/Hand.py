from treys import Evaluator

from src import SoundPlayer
from src.Card import Card
from src.enums.Rank import Rank
from src.enums.Suit import Suit


class Hand:
    """
    This class represents a player's hand (hand, as in poker terms, not biologically)
    """

    def __init__(self):
        self.cards = []
        self.evaluator = Evaluator()
        self.eval_fill_cards = [Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.KING), Card(Suit.CLUB, Rank.EIGHT)]

    def __str__(self) -> str:
        """
        Returns the cards in the hand descriptively; separated by a comma.

        :return: the cards in the hand descriptively; separated by a comma
        """

        ret = ''
        for card in self.cards:
            ret += str(card) + ', '

        return ret[:-2]

    def add_card(self, card: Card) -> "Hand":
        """
        :param card: the card to add to the hand.
        :return: the hand (itself)
        """

        self.cards.append(card)
        SoundPlayer.play_deal_sound()
        return self

    def empty(self):
        self.cards = []

    def evaluate(self) -> int:
        """
        Evaluates the hand's strength using Treys library.

        :return: the strength of the hand
        """

        if len(self.cards) < 5:
            cards = []
            cards.extend(self.eval_fill_cards)
            cards.extend(self.cards)
        else:
            cards = self.cards

        return self.evaluator.evaluate([card.as_treys_card() for card in cards], [])

    def is_empty(self) -> bool:
        return len(self.cards) == 0
