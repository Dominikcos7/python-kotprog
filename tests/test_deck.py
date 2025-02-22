import unittest

from src.Card import Card
from src.Deck import Deck
from src.enums.Rank import Rank
from src.enums.Suit import Suit


class TestDeck(unittest.TestCase):
    def test_init_deck_content(self):
        deck = Deck()
        expected = []
        for suit in Suit:
            for rank in Rank:
                expected.append(Card(suit, rank))

        self.assertEqual(set(expected), set(deck.cards), "Deck should contain all cards initially.")

    def test_init_deck_size(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52, "Deck size should be 52 initially.")

    def test_deck_duplicates(self):
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52, "Deck should not contain duplicate cards.")

    def test_draw_from_non_empty_deck(self):
        deck = Deck()
        initial = len(deck.cards)
        deck.draw()
        after_draw = len(deck.cards)
        self.assertEqual(after_draw, initial-1, "Deck should contain one less card after drawing a card.")

    def test_draw_from_empty_deck(self):
        deck = Deck()
        deck.cards = []
        self.assertRaises(ValueError, deck.draw)

    def test_shuffle_cards(self):
        deck = Deck()
        deck.shuffle()
        deck2 = Deck()
        eq = True

        for c1, c2 in zip(deck.cards, deck2.cards):
            if c1 != c2:
                eq = False
                break

        self.assertFalse(eq, "Shuffle should rearrange cards.")

    def test_shuffle_card_count(self):
        deck = Deck()
        deck.shuffle()
        self.assertEqual(len(deck.cards), 52, "Shuffling the cards should not add or remove cards from deck.")

    def test_shuffle_incomplete_deck(self):
        deck = Deck()
        deck.draw()
        self.assertRaises(ValueError, deck.shuffle)


if __name__ == '__main__':
    unittest.main()
