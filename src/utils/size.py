from typing import NamedTuple, Union


class Size(NamedTuple):
    width: int | float
    height: int | float

    def __sub__(self, other: Union["Size", int, float]) -> "Size":
        if isinstance(other, Size):
            return Size(self.width - other.width, self.height - other.height)
        return Size(self.width - other, self.height - other)
