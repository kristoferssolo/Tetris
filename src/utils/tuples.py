from typing import NamedTuple, Union


class Size(NamedTuple):
    """
    A size object.

    Attributes:
        width: The width of the object.
        height: The height of the object.
    """

    width: int | float
    height: int | float

    def __sub__(self, other: Union["Size", int, float]) -> "Size":
        if isinstance(other, Size):
            return Size(self.width - other.width, self.height - other.height)
        return Size(self.width - other, self.height - other)


class BestMove(NamedTuple):
    """
    A best move object.

    Attributes:
        rotation: The rotation of the best move.
        x_axis_offset: The x-axis offset of the best move.
    """

    rotation: int
    x_axis_offset: int
