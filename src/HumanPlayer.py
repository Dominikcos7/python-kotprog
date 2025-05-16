from src.Player import Player


class HumanPlayer(Player):
    """
    This class represents the human player.
    """

    def __init__(self, name: str, chips: int, player_id: int = 0):
        """
        :param name: the name of the player
        :param chips: the amount of chips the player has
        :param player_id: the id of the player
        """

        super().__init__(name, chips, player_id)
        self.is_raising = False
        self.raise_amount_str = ''

    def action_raise(self, call_amount: int) -> None:
        """
        This function is different from other player classes' raise functions, as it takes in the call amount for
        validation purposes.

        :param call_amount: the amount to call
        """

        amount = int(self.raise_amount_str)
        super().action_raise(amount, call_amount)
        self.is_raising = False
        self.raise_amount_str = ''

    def start_raise(self) -> None:
        """
        This is a helper function for the game to know how to handle inputs.
        """

        self.is_raising = True
