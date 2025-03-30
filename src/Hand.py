import treys
from treys import Evaluator

from src import SoundPlayer
from src.Card import Card
from src.enums.Rank import Rank
from src.enums.Suit import Suit


class Hand:
    def __init__(self):
        self.cards = []
        self.evaluator = Evaluator()
        self.eval_fill_cards = [Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.KING), Card(Suit.CLUB, Rank.EIGHT)]

    def __str__(self) -> str:
        ret = ''
        for card in self.cards:
            ret += str(card) + ', '

        return ret[:-2]

    def add_card(self, card: Card) -> "Hand":
        self.cards.append(card)
        SoundPlayer.play_deal_sound()
        return self

    def empty(self):
        self.cards = []

    def evaluate(self) -> int:
        if len(self.cards) < 5:
            cards = []
            cards.extend(self.eval_fill_cards)
            cards.extend(self.cards)
        else:
            cards = self.cards

        return self.evaluator.evaluate([card.as_treys_card() for card in cards], [])

    def is_empty(self) -> bool:
        return len(self.cards) == 0
