from pathlib import Path

from attr import define, field
from pygame import Vector2 as Vec2

from .colors import TokyoNightNight
from .path import BASE_PATH
from .size import Size

PADDING = 20


@define
class Game:
    columns: int = 10
    rows: int = 20
    line_width: int = 1
    border_radius: int = 5
    padding: int = PADDING
    cell: Size = Size(40, 40)
    size: Size = Size(columns * cell.width, rows * cell.width)
    pos: Vec2 = Vec2(padding, padding)
    offset: Vec2 = Vec2(columns // 2, -1)
    initial_speed: float | int = 50
    movment_delay: int = 200
    rotation_delay: int = 200
    score: dict[int, int] = {1: 40, 2: 100, 3: 300, 4: 1200}


@define
class SideBar:
    padding: int = PADDING
    size: Size = Size(200, Game().size.height)
    score: Size = Size(size.width, size.height * 0.3 - padding)
    preview: Size = Size(size.width, size.height * 0.7)


@define
class Font:
    family: Path = BASE_PATH / "assets" / "fonts" / "ChakraPetch" / "Regular.ttf"
    size: int = 32


@define
class Window:
    title: str = "Tetris"
    padding: int = PADDING
    size: Size = Size(
        Game().size.width + SideBar().size.width + padding * 3,
        Game().size.height + padding * 2,
    )


@define
class Music:
    background: Path = BASE_PATH / "assets" / "music" / "background.wav"
    landing: Path = BASE_PATH / "assets" / "music" / "landing.wav"
    volume: float = 0.01


@define
class AI:
    generations: int = 200
    parallels: int = 1
    winner_path: Path = BASE_PATH / "winner"
    plot_path: Path = BASE_PATH / "plots"
    checkpoint_path: Path = BASE_PATH / "checkpoints"
    config_path: Path = BASE_PATH / "config"
    checkpoint_interval: int = 10
    checkpoint_delay: int = 900


@define
class Config:
    log_level: str = "warning"

    game: Game = Game()
    sidebar: SideBar = SideBar()
    window: Window = Window()
    font: Font = Font()
    music: Music = Music()
    colors = TokyoNightNight()
    ai = AI()
    fps: int = 60


CONFIG = Config()
