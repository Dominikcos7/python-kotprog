import unittest

from src.Card import Card
from src.Player import Player
from src.enums.Rank import Rank
from src.enums.Suit import Suit


def init_player() -> "Player":
    player = Player("bob", 1000)
    return player


def init_player_with_cards_in_hand() -> Player:
    player = Player("bob", 1000)
    player.hand.add_card(Card(Suit.DIAMOND, Rank.SEVEN))
    player.hand.add_card(Card(Suit.HEART, Rank.NINE))
    return player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = init_player()

    def test_call(self):
        chips_before_call = self.player.chips
        chips_on_table_before_call = self.player.chips_on_table

        amount = chips_before_call - 100
        self.player.action_call(amount)

        self.assertEqual(self.player.chips, chips_before_call - amount,
                         "Player should have {amount} less chips than before calling.")
        self.assertEqual(self.player.chips_on_table, chips_on_table_before_call + amount,
                         "Player should have {amount} more chips on table than before calling.")

    def test_call_without_coverage(self):
        chips_before_call = self.player.chips
        chips_on_table_before_call = self.player.chips_on_table

        amount = chips_before_call + 100
        self.player.action_call(amount)

        self.assertEqual(self.player.chips, 0, "Player should have no chips left after all-in (call with no coverage).")
        self.assertEqual(self.player.chips_on_table, chips_before_call + chips_on_table_before_call,
                         "Player should have all their money on the table.")

    def test_fold(self):
        player = init_player_with_cards_in_hand()
        player.action_fold()
        self.assertTrue(player.hand.is_empty())

    def test_raise(self):
        chips_before_raise = self.player.chips
        chips_on_table_before_raise = self.player.chips_on_table

        amount = chips_before_raise - 100
        self.player.action_raise(amount)

        expected_chips_after_raise = chips_before_raise - amount
        actual_chips_after_raise = self.player.chips
        expected_chips_on_table_after_raise = chips_on_table_before_raise + amount
        actual_chips_on_table_after_raise = self.player.chips_on_table

        self.assertEqual(expected_chips_after_raise, actual_chips_after_raise,
                         "Player should have {amount} less chips than before raise.")
        self.assertEqual(expected_chips_on_table_after_raise, actual_chips_on_table_after_raise,
                         "Player should have {amount} more chips on table than before raise.")

    def test_raise_with_not_enough_chips_to_raise(self):
        amount = self.player.chips + 100
        self.assertRaises(ValueError, self.player.action_raise, amount)

    def test_all_in(self):
        chips_before_all_in = self.player.chips
        chips_on_table_before_all_in = self.player.chips_on_table

        self.player.action_all_in()

        expected_chips = 0
        actual_chips = self.player.chips
        expected_chips_on_table = chips_before_all_in + chips_on_table_before_all_in
        actual_chips_on_table = self.player.chips_on_table

        self.assertEqual(expected_chips, actual_chips, "Player should have no chips left after all in.")
        self.assertEqual(expected_chips_on_table, actual_chips_on_table, "Player should have all their money on the table.")

    def test_call_with_player_having_negative_chips(self):
        self.player.chips = -1
        self.assertRaises(ValueError, self.player.action_call, 100)

    def test_call_would_result_in_negative_chips(self):
        amount = self.player.chips + 1000
        self.player.action_call(amount)
        self.assertGreaterEqual(self.player.chips, 0)

    def test_call_with_negative_amount(self):
        self.assertRaises(ValueError, self.player.action_call, -1)

    def test_call_with_zero_amount(self):
        self.assertRaises(ValueError, self.player.action_call, 0)

    def test_raise_with_player_having_negative_chips(self):
        self.player.chips = -1
        self.assertRaises(ValueError, self.player.action_raise, 100)

    def test_raise_would_result_in_negative_chips(self):
        amount = self.player.chips + 1000
        self.player.action_call(amount)
        self.assertGreaterEqual(self.player.chips, 0)

    def test_raise_with_negative_amount(self):
        self.assertRaises(ValueError, self.player.action_raise, -1)

    def test_raise_with_zero_amount(self):
        self.assertRaises(ValueError, self.player.action_raise, 0)


if __name__ == '__main__':
    unittest.main()
