from pathlib import Path

from attr import define
from pygame import Vector2 as Vec2

from .colors import COLOR_DICT, TokyoNightNight
from .colors.tokyonight.base import Color
from .path import BASE_PATH
from .settings import read_settings
from .tuples import Size

PADDING = 20


@define
class Game:
    """
    Attributes:
        columns: The number of columns.
        rows: The number of rows.
        line_width: The width of the lines.
        border_radius: The radius of the border.
        padding: The padding.
        cell: The size of a cell.
        size: The size of the game.
        pos: The position of the game.
        offset: The offset of the game.
        initial_speed: The initial speed of the game.
        movment_delay: The delay of the movment.
        rotation_delay: The delay of the rotation.
        drop_delay: The delay of the drop.
        score: The score.
        highscore: The path to the highscore file.
        fps: The FPS.

    """

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
    movment_delay: int = 130
    rotation_delay: int = 200
    drop_delay: int = 200
    score: dict[int, int] = {1: 40, 2: 100, 3: 300, 4: 1200}
    highscore: Path = BASE_PATH / "assets" / "highscore"
    fps: int = 60


@define
class SideBar:
    """
    Attributes:
        padding: The padding.
        size: The size of the sidebar.
        score: The size of the score.
        preview: The size of the preview.
    """

    padding: int = PADDING
    size: Size = Size(200, Game().size.height)
    score: Size = Size(size.width, size.height - size.width - padding)
    preview: Size = Size(size.width, size.width)


@define
class Font:
    """
    Attributes:
        family: The font family.
        size: The font size.
    """

    family: Path = BASE_PATH / "assets" / "fonts" / "ChakraPetch" / "Regular.ttf"
    size: int = 32


@define
class Button:
    """
    Attributes:
        size: The size of the button.
    """

    size: Size = Size(200, 50)


@define
class Window:
    """
    Attributes:
        title: The title of the window.
        padding: The padding.
        size: The size of the window.
        button: The button.
    """

    title: str = "Tetris"
    padding: int = PADDING
    size: Size = Size(
        Game().size.width + SideBar().size.width + padding * 3,
        Game().size.height + padding * 2,
    )
    button: Button = Button()


@define
class Music:
    """
    Attributes:
        background: The background music.
        landing: The landing music.
    """

    background: Path = BASE_PATH / "assets" / "music" / "background.mp3"
    landing: Path = BASE_PATH / "assets" / "music" / "landing.wav"


@define
class Config:
    """
    Attributes:
        game: The game.
        sidebar: The sidebar.
        window: The window.
        font: The font.
        music: The music.
        colors: The colors.
    """

    game: Game = Game()
    sidebar: SideBar = SideBar()
    window: Window = Window()
    font: Font = Font()
    music: Music = Music()
    colors: Color = COLOR_DICT.get(read_settings()["General"]["colorscheme"], TokyoNightNight)()


CONFIG = Config()
