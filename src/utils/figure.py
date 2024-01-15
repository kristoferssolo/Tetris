import random
from enum import Enum
from typing import NamedTuple

import pygame
from pygame import Vector2 as Vec2

from .colors import TokyoNightNight
from .path import BASE_PATH


class FigureConfig(NamedTuple):
    """
    Attributes:
        shape: The shape of the figure.
        color: The color of the figure.
        filename: The filename of the image of the figure.
        image: The image of the figure.
    """

    shape: list[Vec2]
    color: str
    filename: str

    @property
    def image(self) -> pygame.Surface:
        # TODO: change colors of images
        return pygame.image.load(BASE_PATH / "assets" / "figures" / self.filename).convert_alpha()


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
        "I.png",
    )
    O = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(1, 0),
            Vec2(1, -1),
        ],
        TokyoNightNight().yellow,
        "O.png",
    )
    T = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(-1, 0),
            Vec2(1, 0),
            Vec2(0, -1),
        ],
        TokyoNightNight().purple,
        "T.png",
    )

    S = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(-1, 0),
            Vec2(0, -1),
            Vec2(1, -1),
        ],
        TokyoNightNight().green,
        "S.png",
    )
    Z = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(1, 0),
            Vec2(0, -1),
            Vec2(-1, -1),
        ],
        TokyoNightNight().red,
        "Z.png",
    )
    J = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, 1),
            Vec2(-1, 1),
        ],
        TokyoNightNight().blue,
        "J.png",
    )
    L = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, 1),
            Vec2(1, 1),
        ],
        TokyoNightNight().orange,
        "L.png",
    )

    @classmethod
    def random(cls) -> "Figure":
        return random.choice(list(cls))
