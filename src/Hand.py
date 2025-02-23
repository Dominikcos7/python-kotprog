from src.Card import Card


class Hand:
    def __init__(self):
        self.cards = []

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

    def is_empty(self) -> bool:
        return len(self.cards) == 0
