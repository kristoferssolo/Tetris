from pathlib import Path

from attr import define
from pygame import Vector2 as Vec2

from .colors import COLOR_DICT
from .path import BASE_PATH
from .settings import read_settings
from .tuples import Size

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
    initial_speed: float | int = 300
    movment_delay: int = 150
    rotation_delay: int = 200
    drop_delay: int = 200
    score: dict[int, int] = {1: 40, 2: 100, 3: 300, 4: 1200}
    highscore: int = 1_000_000  # TODO: read from file


@define
class SideBar:
    padding: int = PADDING
    size: Size = Size(200, Game().size.height)
    score: Size = Size(size.width, size.height - size.width - padding)
    preview: Size = Size(size.width, size.width)


@define
class Font:
    family: Path = BASE_PATH / "assets" / "fonts" / "ChakraPetch" / "Regular.ttf"
    size: int = 32


@define
class Button:
    size: Size = Size(200, 50)


@define
class Window:
    title: str = "Tetris"
    padding: int = PADDING
    size: Size = Size(
        Game().size.width + SideBar().size.width + padding * 3,
        Game().size.height + padding * 2,
    )
    button: Button = Button()


@define
class Music:
    background: Path = BASE_PATH / "assets" / "music" / "background.mp3"
    landing: Path = BASE_PATH / "assets" / "music" / "landing.wav"


@define
class Checkpoint:
    generation_interval: int = 10
    time_interval: float = 900
    filename_prefix: str = str(BASE_PATH / "checkpoints" / "neat-checkpoint-")


@define
class AI:
    generations: int = 200
    parallels: int = 1
    winner_path: Path = BASE_PATH / "winner"
    plot_path: Path = BASE_PATH / "plots"
    config_path: Path = BASE_PATH / "config"
    checkpoint: Checkpoint = Checkpoint()


@define
class Config:
    log_level: str = "warning"

    game: Game = Game()
    sidebar: SideBar = SideBar()
    window: Window = Window()
    font: Font = Font()
    music: Music = Music()
    colors = COLOR_DICT[read_settings()["General"]["colorscheme"]]()

    ai = AI()
    fps: int = 60


CONFIG = Config()
