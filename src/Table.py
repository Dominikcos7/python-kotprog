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
        self.community_cards = list()
        self.actor_idx = 0
        self.round_winner = None

    def bump_actor_idx(self) -> None:
        if len(self.get_not_folded_players()) < 1:
            return

        self.actor_idx += 1
        if self.actor_idx >= len(self.players):
            self.actor_idx = 0

        if self.players[self.actor_idx].is_folded():
            self.bump_actor_idx()

    def collect_pot(self) -> None:
        for player in self.players:
            self.pot += player.chips_on_table
            player.chips_on_table = 0

    def deal_community_cards(self, amount: int) -> None:
        cards = [self.deck.draw() for _ in range(amount)]

        for card in cards:
            self.community_cards.append(card)
            for player in self.get_not_folded_players():
                player.hand.add_card(card)

    def deal_pocket_cards(self) -> None:
        for player in self.players:
            player.hand.add_card(self.deck.draw()).add_card(self.deck.draw())

    def enter_state(self, state: TableState) -> None:
        match state:
            case TableState.INIT_ROUND:
                if self.state != TableState.CLOSE_ROUND:
                    raise ValueError("Init round state can only be entered from close round state.")

                self.state = TableState.INIT_ROUND
                self.kick_busted_players()
                self.round_winner = None
                self.pot = 0
                self.fold_all_players()
                self.community_cards = []
                self.deck = self.init_deck()
                self.shift_players()
                self.reset_players_last_action()
                self.reset_players_all_in_state()

            case TableState.PRE_FLOP:
                if self.state != TableState.INIT_ROUND:
                    raise ValueError("Pre-flop state can only be entered from init round state.")

                self.state = TableState.PRE_FLOP
                self.deal_pocket_cards()
                self.put_blinds_in()
                self.actor_idx = 2 if len(self.players) > 2 else 0

            case TableState.FLOP:
                if self.state != TableState.PRE_FLOP:
                    raise ValueError("Flop state can only be entered from pre-flop state.")

                self.state = TableState.FLOP
                self.collect_pot()
                self.deal_community_cards(3)
                self.actor_idx = 0

            case TableState.TURN:
                if self.state != TableState.FLOP:
                    raise ValueError("Turn state can only be entered from flop state.")

                self.state = TableState.TURN
                self.collect_pot()
                self.deal_community_cards(1)
                self.actor_idx = 0

            case TableState.RIVER:
                if self.state != TableState.TURN:
                    raise ValueError("River state can only be entered from turn state.")

                self.state = TableState.RIVER
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

                if self.state == TableState.RIVER and len(not_folded_players) > 1 and not self.every_player_called_or_all_in():
                    raise ValueError(
                        "Close round state cannot be entered if table is in river state, more than one player haven't folded and not everyone has called the largest bid.")

                self.state = TableState.CLOSE_ROUND
                self.collect_pot()
                self.round_winner = self.find_winner()
                self.round_winner.chips += self.pot

    def every_player_acted(self) -> bool:
        for player in self.get_not_folded_players():
            if not player.acted:
                return False

        return True

    def every_player_called_or_all_in(self) -> bool:
        amount = self.get_highest_bid()
        for player in self.get_not_folded_players():
            if player.chips_on_table != amount and not player.is_all_in:
                return False

        return True

    def enter_next_state(self) -> None:
        if self.state != TableState.INIT_ROUND and self.state != TableState.CLOSE_ROUND:
            not_folded_players = self.get_not_folded_players()
            if len(not_folded_players) <= 1:
                self.enter_state(TableState.CLOSE_ROUND)
                return

            if not self.every_player_acted():
                raise ValueError("Entering next state is only allowed if every not folded player acted.")

            if not self.every_player_called_or_all_in():
                raise ValueError("Next state can only be entered if every player called.")

        match self.state:
            case TableState.INIT_ROUND:
                self.enter_state(TableState.PRE_FLOP)
            case TableState.PRE_FLOP:
                self.enter_state(TableState.FLOP)
            case TableState.FLOP:
                self.enter_state(TableState.TURN)
            case TableState.TURN:
                self.enter_state(TableState.RIVER)
            case TableState.RIVER:
                self.enter_state(TableState.CLOSE_ROUND)
            case TableState.CLOSE_ROUND:
                self.enter_state(TableState.INIT_ROUND)

        self.set_players_acted_false()

    def find_winner(self) -> "Player":
        not_folded_players = self.get_not_folded_players()
        winner = not_folded_players[0]
        for player in not_folded_players[1:]:
            if player.hand.evaluate() < winner.hand.evaluate():
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
        ret = [player for player in self.players if not player.is_folded()]

        return ret

    def init_deck(self) -> "Deck":
        return Deck().shuffle()

    def kick_busted_players(self) -> None:
        self.players = [player for player in self.players if player.chips > 0]

    def put_blinds_in(self) -> None:
        small_blind = self.players[0]
        small_blind.put_chips_on_table(self.small_blind)

        big_blind = self.players[1]
        big_blind.put_chips_on_table(self.big_blind)

    def reset_players_all_in_state(self):
        for player in self.players:
            player.is_all_in = False

    def reset_players_last_action(self):
        for player in self.players:
            player.last_action = ''

    def set_players_acted_false(self) -> None:
        for player in self.players:
            player.acted = False

    def shift_players(self):
        self.players.append(self.players.pop(0))
