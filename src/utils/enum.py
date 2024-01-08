from enum import Enum, auto


class Direction(Enum):
    """
    Enum for direction of movement.

    Attributes:
        LEFT: Left direction
        RIGHT: Right direction
        DOWN: Down direction
        UP: Up direction
    """

    LEFT = -1
    RIGHT = 1
    DOWN = 1
    UP = -1


class Rotation(Enum):
    """
    Enum for rotation of movement.

    Attributes:
        CLOCKWISE: Clockwise rotation
        COUNTER_CLOCKWISE: Counter clockwise rotation
    """

    CLOCKWISE = 90
    COUNTER_CLOCKWISE = -90


class GameMode(Enum):
    """
    Enum for game mode.

    Attributes:
        PLAYER: Player mode
        AI_PLAYING: AI playing mode
        AI_TRAINING: AI training mode
    """

    PLAYER = auto()
    AI_PLAYING = auto()
    AI_TRAINING = auto()
