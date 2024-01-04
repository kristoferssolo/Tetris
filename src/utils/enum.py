from enum import Enum


class Direction(Enum):
    LEFT = -1
    RIGHT = 1
    DOWN = 1
    UP = -1


class Field(Enum):
    EMPTY = None
    FILLED = "Block"
