from src.Deck import Deck
from src.Player import Player
from src.enums.TableState import TableState


class Table:
    def __init__(self, players: list[Player], blind: int):
        self.players = players
        self.state = TableState.INIT_ROUND
        self.small_blind = blind // 2
        self.big_blind = blind
        self.deck = self.init_deck()
        self.pot = 0
        self.community_cards = []
        self.actor_idx = 2

    def collect_pot(self) -> None:
        for player in self.players:
            self.pot += player.chips_on_table
            player.chips_on_table = 0

    def deal_community_cards(self, amount: int) -> None:
        cards = [self.deck.draw() for _ in range(amount)]
        self.community_cards.append(card for card in cards)

        for player in self.get_not_folded_players():
            for card in cards:
                player.hand.add_card(card)

    def deal_pocket_cards(self) -> None:
        for player in self.players:
            player.hand.add_card(self.deck.draw()).add_card(self.deck.draw())

    def every_player_called(self) -> bool:
        amount = self.get_highest_bid()
        for player in self.get_not_folded_players():
            if player.chips_on_table != amount:
                return False

        return True

    def enter_state(self, state: TableState) -> None:
        match state:
            case TableState.INIT_ROUND:
                if self.state != TableState.CLOSE_ROUND:
                    raise ValueError("Init round state can only be entered from close round state.")

                not_folded_players = self.get_not_folded_players()
                if len(not_folded_players) > 0:
                    raise ValueError("Init round state cannot be entered if any player has a card.")

                self.deck = self.init_deck()
                self.shift_players()

            case TableState.PRE_FLOP:
                if self.state != TableState.INIT_ROUND:
                    raise ValueError("Pre-flop state can only be entered from init round state.")

                self.deal_pocket_cards()
                self.put_blinds_in()
                self.actor_idx = 2

            case TableState.FLOP:
                if self.state != TableState.PRE_FLOP:
                    raise ValueError("Flop state can only be entered from pre-flop state.")

                if not self.every_player_called():
                    raise ValueError("Flop state can only be entered if every player called.")

                not_folded_players = self.get_not_folded_players()
                if len(not_folded_players) <= 1:
                    raise ValueError("Flop state can only be entered if at least two players haven't folded.")

                self.collect_pot()
                self.deal_community_cards(3)
                self.actor_idx = 0

            case TableState.TURN:
                if self.state != TableState.FLOP:
                    raise ValueError("Turn state can only be entered from flop state.")

                if not self.every_player_called():
                    raise ValueError("Turn state can only be entered if every player called.")

                not_folded_players = self.get_not_folded_players()
                if len(not_folded_players) <= 1:
                    raise ValueError("Turn state can only be entered if at least two players haven't folded.")

                self.collect_pot()
                self.deal_community_cards(1)
                self.actor_idx = 0

            case TableState.RIVER:
                if self.state != TableState.TURN:
                    raise ValueError("River state can only be entered from turn state.")

                if not self.every_player_called():
                    raise ValueError("River state can only be entered if every player called.")

                not_folded_players = self.get_not_folded_players()
                if len(not_folded_players) <= 1:
                    raise ValueError("River state can only be entered if at least two players haven't folded.")

                self.collect_pot()
                self.deal_community_cards(1)
                self.actor_idx = 0

            case TableState.CLOSE_ROUND:
                if self.state == TableState.INIT_ROUND:
                    raise ValueError("Close round state cannot be entered from init round state.")

                not_folded_players = self.get_not_folded_players()
                if self.state != TableState.RIVER and len(not_folded_players) > 1:
                    raise ValueError(
                        "Close round state cannot be entered if table is in river state and more than one player haven't folded.")

                if self.state == TableState.RIVER and len(not_folded_players) > 1 and not self.every_player_called():
                    raise ValueError(
                        "Close round state cannot be entered if table is in river state, more than one player haven't folded and not everyone has called the largest bid.")

                self.collect_pot()
                winner = self.find_winner()
                winner.chips += self.pot
                self.fold_all_players()

    def find_winner(self) -> "Player":
        not_folded_players = self.get_not_folded_players()
        winner = not_folded_players[0]
        for player in not_folded_players[1:]:
            if player.hand.evaluate() > winner.hand.evaluate():
                winner = player

        return winner

    def fold_all_players(self) -> None:
        for player in self.players:
            player.action_fold()

    def get_acting_player(self) -> Player:
        return self.players[self.actor_idx]

    def get_highest_bid(self) -> int:
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

    def init_deck(self) -> "Deck":
        return Deck().shuffle()

    def put_blinds_in(self) -> None:
        small_blind = self.players[0]
        small_blind.put_chips_on_table(self.small_blind)

        big_blind = self.players[1]
        big_blind.put_chips_on_table(self.big_blind)

    def shift_players(self):
        self.players.append(self.players.pop(0))
