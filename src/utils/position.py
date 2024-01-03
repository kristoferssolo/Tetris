from typing import NamedTuple, Union


class Position(NamedTuple):
    x: int | float
    y: int | float

    def add(self, other: Union["Position", int, float]) -> "Position":
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        return Position(self.x + other, self.y + other)

    def sub(self, other: Union["Position", int, float]) -> "Position":
        if isinstance(other, Position):
            return Position(self.x - other.x, self.y - other.y)
        return Position(self.x - other, self.y - other)

    def add_x(self, other: Union["Position", int, float]) -> "Position":
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y)
        return Position(self.x + other, self.y)

    def add_y(self, other: Union["Position", int, float]) -> "Position":
        if isinstance(other, Position):
            return Position(self.x, self.y + other.y)
        return Position(self.x, self.y + other)

    def sub_x(self, other: Union["Position", int, float]) -> "Position":
        if isinstance(other, Position):
            return Position(self.x - other.x, self.y)
        return Position(self.x - other, self.y)

    def sub_y(self, other: Union["Position", int, float]) -> "Position":
        if isinstance(other, Position):
            return Position(self.x, self.y - other.y)
        return Position(self.x, self.y - other)

    def to_grid(self) -> "Position":
        from .config import CONFIG

        return Position(
            self.x * CONFIG.game.cell.width, self.y * CONFIG.game.cell.height
        )
