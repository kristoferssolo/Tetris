from typing import NamedTuple

from attr import define

from .colors import TokyoNightNight


class Size(NamedTuple):
    width: int
    height: int


@define
class Game:
    columns: int = 10
    rows: int = 20
    cell_size: int = 40
    size: Size = Size(columns * cell_size, rows * cell_size)


@define
class SideBar:
    size: Size = Size(200, Game().size.height)
    preview_height_fraction: float = 0.7
    score_height_fraction: float = 1 - preview_height_fraction


@define
class Window:
    title = "Tetris"
    padding: int = 20
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
