from typing import NamedTuple, Union

from attr import define, field

from .colors import TokyoNightNight

PADDING = 20


class Size(NamedTuple):
    width: int | float
    height: int | float

    def add(self, other: Union["Size", int, float]) -> "Size":
        if isinstance(other, Size):
            return Size(self.width + other.width, self.height + other.height)
        return Size(self.width + other, self.height + other)

    def sub(self, other: Union["Size", int, float]) -> "Size":
        if isinstance(other, Size):
            return Size(self.width - other.width, self.height - other.height)
        return Size(self.width - other, self.height - other)


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


@define
class Game:
    columns: int = 10
    rows: int = 20
    padding: int = PADDING
    cell_size: int = 40
    size: Size = Size(columns * cell_size, rows * cell_size)
    pos: Position = Position(padding, padding)


@define
class SideBar:
    padding: int = PADDING
    size: Size = Size(200, Game().size.height)
    score: Size = Size(size.width, size.height * 0.3 - padding)
    preview: Size = Size(size.width, size.height * 0.7)


@define
class Window:
    title = "Tetris"
    padding: int = PADDING
    size: Size = Size(
        Game().size.width + SideBar().size.width + padding * 3,
        Game().size.height + padding * 2,
    )


@define
class Config:
    log_level: str = "warning"

    game: Game = Game()
    sidebar: SideBar = SideBar()
    window: Window = Window()
    colors = TokyoNightNight()
    fps: int = 60


CONFIG = Config()
