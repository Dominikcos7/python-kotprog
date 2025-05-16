from enum import Enum


class TableState(Enum):
    """
    Represents the states a table can have in the game. These states dictate the flow of the game and allow specific
    checks to happen when a player does an action.
    """

    INIT_ROUND = 0
    PRE_FLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4
    CLOSE_ROUND = 5
