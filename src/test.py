from treys.evaluator import Evaluator
from treys.card import Card as tCard

from src.Deck import Deck
from src.Hand import Hand
from src.enums.Rank import Rank

if __name__ == '__main__':
    deck = Deck().shuffle()
    hand = Hand()
    hand.add_card(deck.draw())
    hand.add_card(deck.draw())
    hand.add_card(deck.draw())
    hand.add_card(deck.draw())
    hand.add_card(deck.draw())
    hand.add_card(deck.draw())
    hand.add_card(deck.draw())
    print(hand.evaluate())
