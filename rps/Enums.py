from enum import IntEnum


class MoveEnum(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class ResultEnum(IntEnum):
    NONE = 0
    P1 = 1
    P2 = 2
    DRAW = 3
