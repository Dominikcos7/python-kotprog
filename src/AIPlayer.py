from abc import ABC, abstractmethod
from src.Player import Player


class AIPlayer(Player, ABC):
    """
    This class is an abstract base class for all AI players.
    """

    def __init__(self, name: str, chips: int, player_id: int):
        """
        :param name: the name of the player
        :param chips: the amount of chips the player has
        :param player_id: the id of the player
        """

        Player.__init__(self, name, chips, player_id)

    @abstractmethod
    def act(self, highest_bid: int) -> None:
        """
        This function is called by the game when a player needs to act (when it's their turn). It needs to be
        implemented in child classes.

        :param highest_bid: the highest bid on the table
        """

        pass
