import unittest

from src.Card import Card
from src.enums.Suit import Suit
from src.enums.Rank import Rank


class CardTest(unittest.TestCase):
    def test_string_representation(self):
        card = Card(Suit.SPADE, Rank.ACE)
        expected = "ace of spades"
        self.assertEqual(str(card), expected, "String representation of card should be: '{rank} of {suit}s'")

    def test_equality(self):
        card1 = Card(Suit.SPADE, Rank.ACE)
        card2 = Card(Suit.SPADE, Rank.ACE)
        self.assertEqual(card1, card2, "Two cards of same rank and suit should be equal")

    def test_inequality(self):
        card1 = Card(Suit.SPADE, Rank.ACE)
        card2 = Card(Suit.SPADE, Rank.TWO)
        self.assertNotEqual(card1, card2, "Two different cards should not be equal")


if __name__ == '__main__':
    unittest.main()
