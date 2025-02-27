from src.Deck import Deck
from src.Player import Player
from src.enums.TableState import TableState


class Table:
    def __init__(self, players: list[Player], blind: int):
        self.players = players

        self.state = TableState.INIT_ROUND

        self.small_blind = blind // 2
        self.big_blind = blind

        self.deck = Deck()
        self.deck.shuffle()

    def every_player_called(self) -> bool:
        amount = self.get_highest_bid()
        for player in self.get_not_folded_players():
            if player.chips_on_table != amount:
                return False

        return True

    def deal_cards_to_players(self):
        for player in self.players:
            player.hand.add_card(self.deck.draw()).add_card(self.deck.draw())

    def enter_state(self, state: TableState):
        match state:
            case TableState.INIT_ROUND:
                pass
            case TableState.PRE_FLOP:
                if self.state != TableState.INIT_ROUND:
                    raise ValueError("Pre-flop state can only be entered from init round state.")

                self.deal_cards_to_players()
                self.put_blinds_in()
            case TableState.FLOP:
                if self.state != TableState.PRE_FLOP:
                    raise ValueError("Flop state can only be entered from pre-flop state.")

                if not self.every_player_called():
                    raise ValueError("Flop state can only be entered if every player called.")

                not_folded_players = self.get_not_folded_players()
                if len(not_folded_players) <= 1:
                    raise ValueError("Flop state can only be entered if at least two players haven't folded.")

                self.flop()

            case TableState.TURN:
                if self.state != TableState.FLOP:
                    raise ValueError("Turn state can only be entered from flop state.")

                if not self.every_player_called():
                    raise ValueError("Turn state can only be entered if every player called.")

                not_folded_players = self.get_not_folded_players()
                if len(not_folded_players) <= 1:
                    raise ValueError("Turn state can only be entered if at least two players haven't folded.")

                self.turn()

    def flop(self):
        flop = [self.deck.draw(), self.deck.draw(), self.deck.draw()]

        for player in self.get_not_folded_players():
            for card in flop:
                player.hand.add_card(card)

    def get_highest_bid(self):
        players = self.get_not_folded_players()
        bid = players[0].chips_on_table
        for player in players[1:]:
            bid = max(bid, player.chips_on_table)

        return bid

    def get_not_folded_players(self) -> list[Player]:
        ret = []
        for player in self.players:
            if len(player.hand.cards) > 0:
                ret.append(player)

        return ret

    def put_blinds_in(self):
        small_blind = self.players[0]
        small_blind.put_chips_on_table(self.small_blind)

        big_blind = self.players[1]
        big_blind.put_chips_on_table(self.big_blind)

    def turn(self):
        turn = self.deck.draw()
        for player in self.get_not_folded_players():
            player.hand.add_card(turn)
