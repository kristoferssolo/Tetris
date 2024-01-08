from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:
    from typing import Union


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
