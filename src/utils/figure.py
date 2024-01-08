import random
from enum import Enum
from typing import TYPE_CHECKING, NamedTuple

import pygame

from .colors import TokyoNightNight
from .path import BASE_PATH

if TYPE_CHECKING:
    from pygame import Vector2 as Vec2


class FigureConfig(NamedTuple):
    """
    Attributes:
        shape: The shape of the figure.
        color: The color of the figure.
        image: The image of the figure.
    """

    shape: list[Vec2]
    color: str
    image: pygame.Surface


def _load_image(filename: str) -> pygame.Surface:
    return pygame.image.load(BASE_PATH / "assets" / "figures" / filename)  # TODO: add `.convert_alpha()``
    # TODO: change colors of images


class Figure(Enum):
    """
    Attributes:
        I: The I figure.
        O: The O figure.
        T: The T figure.
        S: The S figure.
        Z: The Z figure.
        J: The J figure.
        L: The L figure.
    """

    I = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, -2),
            Vec2(0, 1),
        ],
        TokyoNightNight().cyan,
        _load_image("I.png"),
    )
    O = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(1, 0),
            Vec2(1, -1),
        ],
        TokyoNightNight().yellow,
        _load_image("O.png"),
    )
    T = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(-1, 0),
            Vec2(1, 0),
            Vec2(0, -1),
        ],
        TokyoNightNight().purple,
        _load_image("T.png"),
    )

    S = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(-1, 0),
            Vec2(0, -1),
            Vec2(1, -1),
        ],
        TokyoNightNight().green,
        _load_image("S.png"),
    )
    Z = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(1, 0),
            Vec2(0, -1),
            Vec2(-1, -1),
        ],
        TokyoNightNight().red,
        _load_image("Z.png"),
    )
    J = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, 1),
            Vec2(-1, 1),
        ],
        TokyoNightNight().blue,
        _load_image("J.png"),
    )
    L = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, 1),
            Vec2(1, 1),
        ],
        TokyoNightNight().orange,
        _load_image("L.png"),
    )

    @classmethod
    def random(cls) -> "Figure":
        return random.choice(list(cls))
