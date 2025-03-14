import unittest

from src.Player import Player
from src.Table import Table
from src.enums.TableState import TableState


class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table([Player("alice", 1000), Player("bob", 1000), Player("charlie", 1000)], 10)

    def test_enter_state_pre_flop(self):
        self.table.state = TableState.PRE_FLOP
        self.assertRaises(ValueError, self.table.enter_state, TableState.PRE_FLOP)
        self.table.state = TableState.FLOP
        self.assertRaises(ValueError, self.table.enter_state, TableState.PRE_FLOP)
        self.table.state = TableState.TURN
        self.assertRaises(ValueError, self.table.enter_state, TableState.PRE_FLOP)
        self.table.state = TableState.RIVER
        self.assertRaises(ValueError, self.table.enter_state, TableState.PRE_FLOP)
        self.table.state = TableState.CLOSE_ROUND
        self.assertRaises(ValueError, self.table.enter_state, TableState.PRE_FLOP)

        self.table.state = TableState.INIT_ROUND
        self.table.enter_state(TableState.PRE_FLOP)

        for player in self.table.players:
            self.assertEqual(2, len(player.hand.cards), "Every player should have 2 cards in their hands pre flop.")

        small_blind = self.table.players[0]
        expected = self.table.small_blind
        actual = small_blind.chips_on_table
        self.assertEqual(expected, actual, "Small blind should have {expected} amount of chips on the table.")

        big_blind = self.table.players[1]
        expected = self.table.big_blind
        actual = big_blind.chips_on_table
        self.assertEqual(expected, actual, "Big blind should have {expected} amount of chips on the table.")

    def test_enter_state_flop(self):
        for player in self.table.players:
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())

        self.table.state = TableState.INIT_ROUND
        self.assertRaises(ValueError, self.table.enter_state, TableState.FLOP)
        self.table.state = TableState.FLOP
        self.assertRaises(ValueError, self.table.enter_state, TableState.FLOP)
        self.table.state = TableState.TURN
        self.assertRaises(ValueError, self.table.enter_state, TableState.FLOP)
        self.table.state = TableState.RIVER
        self.assertRaises(ValueError, self.table.enter_state, TableState.FLOP)
        self.table.state = TableState.CLOSE_ROUND
        self.assertRaises(ValueError, self.table.enter_state, TableState.FLOP)

        self.table.state = TableState.PRE_FLOP
        for player in self.table.players:
            player.put_chips_on_table(100)

        self.table.players[0].put_chips_on_table(100)
        # raise error if every player who hasn't folded hasn't called the highest bid
        self.assertRaises(ValueError, self.table.enter_state, TableState.FLOP)

        for player in self.table.players[1:]:
            player.action_fold()
        # raise error if only one player hasn't folded (the round is over)
        self.assertRaises(ValueError, self.table.enter_state, TableState.FLOP)

        for player in self.table.players:
            player.action_fold()
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.chips = 1000
            player.chips_on_table = 0
            player.put_chips_on_table(100)

        self.table.enter_state(TableState.FLOP)

        for player in self.table.players:
            cards_count = len(player.hand.cards)
            self.assertTrue(cards_count == 0 or cards_count == 5, "Every player should have 0 (if folded) or 5 cards in their hands at flop.")

    def test_enter_state_turn(self):
        for player in self.table.players:
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.hand.add_card(self.table.deck.draw())

        self.table.state = TableState.INIT_ROUND
        self.assertRaises(ValueError, self.table.enter_state, TableState.TURN)
        self.table.state = TableState.PRE_FLOP
        self.assertRaises(ValueError, self.table.enter_state, TableState.TURN)
        self.table.state = TableState.TURN
        self.assertRaises(ValueError, self.table.enter_state, TableState.TURN)
        self.table.state = TableState.RIVER
        self.assertRaises(ValueError, self.table.enter_state, TableState.TURN)
        self.table.state = TableState.CLOSE_ROUND
        self.assertRaises(ValueError, self.table.enter_state, TableState.TURN)

        self.table.state = TableState.FLOP
        for player in self.table.players:
            player.put_chips_on_table(100)

        self.table.players[0].put_chips_on_table(100)
        # raise error if every player who hasn't folded hasn't called the highest bid
        self.assertRaises(ValueError, self.table.enter_state, TableState.TURN)

        for player in self.table.players[1:]:
            player.action_fold()
        # raise error if only one player hasn't folded (the round is over)
        self.assertRaises(ValueError, self.table.enter_state, TableState.TURN)

        for player in self.table.players:
            player.action_fold()
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.hand.add_card(self.table.deck.draw())
            player.chips = 1000
            player.chips_on_table = 0
            player.put_chips_on_table(100)

        self.table.enter_state(TableState.TURN)

        for player in self.table.players:
            cards_count = len(player.hand.cards)
            self.assertTrue(cards_count == 0 or cards_count == 6, "Every player should have 0 (if folded) or 6 cards in their hands at turn.")

    def test_enter_state_river(self):
        for player in self.table.players:
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.hand.add_card(self.table.deck.draw())

        self.table.state = TableState.INIT_ROUND
        self.assertRaises(ValueError, self.table.enter_state, TableState.RIVER)
        self.table.state = TableState.PRE_FLOP
        self.assertRaises(ValueError, self.table.enter_state, TableState.RIVER)
        self.table.state = TableState.FLOP
        self.assertRaises(ValueError, self.table.enter_state, TableState.RIVER)
        self.table.state = TableState.RIVER
        self.assertRaises(ValueError, self.table.enter_state, TableState.RIVER)
        self.table.state = TableState.CLOSE_ROUND
        self.assertRaises(ValueError, self.table.enter_state, TableState.RIVER)

        self.table.state = TableState.TURN
        for player in self.table.players:
            player.put_chips_on_table(100)

        self.table.players[0].put_chips_on_table(100)
        # raise error if every player who hasn't folded hasn't called the highest bid
        self.assertRaises(ValueError, self.table.enter_state, TableState.RIVER)

        for player in self.table.players[1:]:
            player.action_fold()
        # raise error if only one player hasn't folded (the round is over)
        self.assertRaises(ValueError, self.table.enter_state, TableState.RIVER)

        for player in self.table.players:
            player.action_fold()
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())
            player.chips = 1000
            player.chips_on_table = 0
            player.put_chips_on_table(100)

        self.table.enter_state(TableState.RIVER)

        for player in self.table.players:
            cards_count = len(player.hand.cards)
            self.assertTrue(cards_count == 0 or cards_count == 7,
                            "Every player should have 0 (if folded) or 7 cards in their hands at river.")

    def test_enter_state_close_round(self):
        self.table.state = TableState.INIT_ROUND
        self.assertRaises(ValueError, self.table.enter_state, TableState.CLOSE_ROUND)

        self.table.state = TableState.PRE_FLOP
        for player in self.table.players:
            player.hand.add_card(self.table.deck.draw()).add_card(self.table.deck.draw())

        # raise error if more than one player haven't folded and table is not after river
        self.assertRaises(ValueError, self.table.enter_state, TableState.CLOSE_ROUND)

        self.table.state = TableState.RIVER
        for player in self.table.players:
            player.put_chips_on_table(100)

        self.table.players[0].put_chips_on_table(100)
        # raise error if table is after river, more than one player haven't folded and not everyone has called
        self.assertRaises(ValueError, self.table.enter_state, TableState.CLOSE_ROUND)

    def test_enter_state_init_round(self):
        self.table.state = TableState.INIT_ROUND
        self.assertRaises(ValueError, self.table.enter_state, TableState.INIT_ROUND)
        self.table.state = TableState.PRE_FLOP
        self.assertRaises(ValueError, self.table.enter_state, TableState.INIT_ROUND)
        self.table.state = TableState.FLOP
        self.assertRaises(ValueError, self.table.enter_state, TableState.INIT_ROUND)
        self.table.state = TableState.RIVER
        self.assertRaises(ValueError, self.table.enter_state, TableState.INIT_ROUND)
        self.table.state = TableState.TURN
        self.assertRaises(ValueError, self.table.enter_state, TableState.INIT_ROUND)

        self.table.state = TableState.CLOSE_ROUND
        self.table.players[0].hand.add_card(self.table.deck.draw())
        # raise error if any player has cards in their hands
        self.assertRaises(ValueError, self.table.enter_state, TableState.INIT_ROUND)

        self.table.players[0].action_fold()
        next_small_blind = self.table.players[1]
        self.table.enter_state(TableState.INIT_ROUND)

        expected_deck_len = 52
        actual_deck_len = len(self.table.deck.cards)
        self.assertEqual(expected_deck_len, actual_deck_len, "Deck should be reset after init round.")

        expected_small_blind = next_small_blind
        actual_small_blind = self.table.players[0]
        self.assertEqual(expected_small_blind, actual_small_blind, "Players should be rotated after init round.")

    def test_collect_pot(self):
        amount = 0
        for player in self.table.players:
            player.put_chips_on_table(100)
            amount += 100

        self.table.collect_pot()
        expected = amount
        actual = self.table.pot

        self.assertEqual(expected, actual, "Table should have money in pot after collecting it.")


if __name__ == '__main__':
    unittest.main()
