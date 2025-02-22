from src.Card import Card


class Hand:
    def __init__(self):
        self._cards = []

    def __str__(self) -> str:
        ret = ''
        for card in self._cards:
            ret += str(card) + ', '

        return ret[:-2]

    def add_card(self, card: Card) -> "Hand":
        self._cards.append(card)
        return self

    def empty(self):
        self._cards = []

    def is_empty(self) -> bool:
        return len(self._cards) == 0
