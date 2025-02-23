import unittest

from src.Card import Card
from src.Hand import Hand
from src.enums.Suit import Suit
from src.enums.Rank import Rank


class TestHand(unittest.TestCase):
    def test_initial_hand_is_empty(self):
        hand = Hand()
        self.assertEqual(len(hand.cards), 0, "Hand should start empty.")

    def test_add_one_card(self):
        hand = Hand()
        card = Card(Suit.DIAMOND, Rank.SEVEN)
        hand.add_card(card)
        self.assertEqual(len(hand.cards), 1, "Hand should contain one card after adding one card.")

    def test_add_multiple_cards(self):
        hand = Hand()
        card = Card(Suit.DIAMOND, Rank.SEVEN)
        card2 = Card(Suit.SPADE, Rank.KING)
        hand.add_card(card)
        hand.add_card(card2)
        self.assertEqual(len(hand.cards), 2, "Hand should contain two cards after adding two cards.")

    def test_string_representation(self):
        hand = Hand()
        card = Card(Suit.DIAMOND, Rank.SEVEN)
        card2 = Card(Suit.SPADE, Rank.KING)
        hand.add_card(card).add_card(card2)
        expected = "seven of diamonds, king of spades"
        self.assertEqual(expected, str(hand), "String representation should match the expected output: '{rank} of {suit}s, {rank} of {suit}s, ...'")

    def test_empty(self):
        hand = Hand()
        hand.add_card(Card(Suit.DIAMOND, Rank.SEVEN))
        hand.add_card(Card(Suit.SPADE, Rank.KING))
        hand.empty()
        self.assertEqual(len(hand.cards), 0, "Hand should be empty after emptying hand.")

    def test_is_empty_with_cards_in_hand(self):
        hand = Hand()
        card = Card(Suit.DIAMOND, Rank.SEVEN)
        card2 = Card(Suit.SPADE, Rank.KING)
        hand.add_card(card).add_card(card2)
        self.assertFalse(hand.is_empty(), "Hand should not be empty with cards in it.")

    def test_is_empty_with_no_cards_in_hand(self):
        hand = Hand()
        self.assertTrue(hand.is_empty(), "Hand should be empty with no cards in it.")


if __name__ == '__main__':
    unittest.main()
