import treys
from treys import Evaluator

from src.Card import Card


class Hand:
    def __init__(self):
        self.cards = []
        self.evaluator = Evaluator()

    def __str__(self) -> str:
        ret = ''
        for card in self.cards:
            ret += str(card) + ', '

        return ret[:-2]

    def add_card(self, card: Card) -> "Hand":
        self.cards.append(card)
        return self

    def empty(self):
        self.cards = []

    def evaluate(self) -> int:
        return self.evaluator.evaluate([card.as_treys_card() for card in self.cards], [])

    def is_empty(self) -> bool:
        return len(self.cards) == 0
