from src.Player import Player


class HumanPlayer(Player):
    def __init__(self, name: str, chips: int, player_id: int = 0):
        super().__init__(name, chips, player_id)
        self.isRaising = False
        self.raise_amount_str = ''

    def action_raise(self, call_amount: int) -> None:
        amount = int(self.raise_amount_str)
        super().action_raise(amount, call_amount)
        self.isRaising = False
        self.raise_amount_str = ''

    def start_raise(self) -> None:
        self.isRaising = True
