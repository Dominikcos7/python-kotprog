import unittest

from src.Card import Card
from src.Hand import Hand
from src.enums.Suit import Suit
from src.enums.Rank import Rank


class HandTest(unittest.TestCase):
    def test_initial_hand_is_empty(self):
        hand = Hand()
        self.assertEqual(len(hand._cards), 0, "Hand should start empty.")

    def test_add_one_card(self):
        hand = Hand()
        card = Card(Suit.DIAMOND, Rank.SEVEN)
        hand.add_card(card)
        self.assertEqual(len(hand._cards), 1, "Hand should contain one card after adding one card.")

    def test_add_multiple_cards(self):
        hand = Hand()
        card = Card(Suit.DIAMOND, Rank.SEVEN)
        card2 = Card(Suit.SPADE, Rank.KING)
        hand.add_card(card)
        hand.add_card(card2)
        self.assertEqual(len(hand._cards), 2, "Hand should contain two cards after adding two cards.")

    def test_string_representation(self):
        hand = Hand()
        card = Card(Suit.DIAMOND, Rank.SEVEN)
        card2 = Card(Suit.SPADE, Rank.KING)
        hand.add_card(card).add_card(card2)
        expected = "seven of diamonds, king of spades"
        self.assertEqual(expected, str(hand), "String representation should match the expected output: '{rank} of {"
                                              "suit}s, {rank} of {suit}s, ...'")


if __name__ == '__main__':
    unittest.main()
