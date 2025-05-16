from src.AIPlayer import AIPlayer


class CheckOrCallPlayer(AIPlayer):
    """
    This class represents a basic AI player. It will always call the highest bid. (Unused in final game, was there to
    test functionality)
    """

    def __init__(self, name: str, chips: int, player_id: int):
        """
        :param name: the name of the player
        :param chips: the amount of chips the player has
        :param player_id: the id of the player
        """

        super().__init__(name, chips, player_id)

    def act(self, highest_bid: int) -> None:
        """
        This function is called by the game when a player needs to act (when it's their turn). CheckOrCall player always
        calls the highest bid.

        :param highest_bid: the highest bid on the table
        """

        try:
            self.action_check(highest_bid)
        except ValueError:
            amount = self.get_amount_to_call(highest_bid)
            self.action_call(amount)
