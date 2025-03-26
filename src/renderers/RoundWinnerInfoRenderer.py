from pygame import Surface

from src.Player import Player
from src.renderers.InfoRenderer import InfoRenderer


class RoundWinnerInfoRenderer(InfoRenderer):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def render_round_winner_info(self, winner: Player, amount: int) -> None:
        rank_class = winner.hand.evaluator.get_rank_class(winner.hand.evaluate())
        winning_hand = winner.hand.evaluator.class_to_string(rank_class)
        text = f"{winner.name} wins {amount} with {winning_hand}!"

        print(text)
        self.render_info(text)
