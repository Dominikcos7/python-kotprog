from pygame import Surface

from src.Card import Card
from src.Player import Player
from src.renderers.InfoRenderer import InfoRenderer


class RoundWinnerInfoRenderer(InfoRenderer):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def render_round_winner_info(self, winner: Player, amount: int, community_cards: list[Card]) -> None:
        rank_class = winner.hand.evaluator.get_rank_class(winner.hand.evaluate())
        winning_hand = winner.hand.evaluator.class_to_string(rank_class)
        text = f"{winner.name} wins {amount} chips"
        if len(community_cards) > 0:
            text += f" with {winning_hand}!"

        self.render_info(text)
