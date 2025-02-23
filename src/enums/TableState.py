from enum import Enum


class TableState(Enum):
    INIT_ROUND = 0
    PRE_FLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4
    CLOSE_ROUND = 5
