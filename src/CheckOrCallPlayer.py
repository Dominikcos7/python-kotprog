from src.AIPlayer import AIPlayer


class CheckOrCallPlayer(AIPlayer):
    def __init__(self, name: str, chips: int, player_id: int):
        super().__init__(name, chips, player_id)

    def act(self, highest_bid: int) -> None:
        try:
            self.action_check(highest_bid)
        except ValueError:
            amount = self.get_amount_to_call(highest_bid)
            self.action_call(amount)
