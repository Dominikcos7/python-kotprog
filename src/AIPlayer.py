from abc import ABC, abstractmethod
from src.Player import Player


class AIPlayer(Player, ABC):
    def __init__(self, name: str, chips: int, player_id: int):
        Player.__init__(self, name, chips, player_id)

    @abstractmethod
    def act(self, highest_bid: int) -> None:
        pass
