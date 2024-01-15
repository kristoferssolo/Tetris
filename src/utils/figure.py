import random
from enum import Enum

import pygame
from attrs import define
from pygame import Vector2 as Vec2

from .config import CONFIG
from .path import BASE_PATH


@define
class FigureParams:
    """
    Attributes:
        shape: The shape of the figure.
        color: The color of the figure.
        filename: The filename of the image of the figure.
    """

    shape: list[Vec2]
    color: str
    filename: str

    def image(self) -> pygame.Surface:
        """
        Returns:
            The image of the figure.
        """
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

    I = FigureParams(  # type: ignore
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, -2),
            Vec2(0, 1),
        ],
        CONFIG.colors.cyan,
        "I.png",
    )
    O = FigureParams(  # type: ignore
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(1, 0),
            Vec2(1, -1),
        ],
        CONFIG.colors.yellow,
        "O.png",
    )
    T = FigureParams(  # type: ignore
        [
            Vec2(0, 0),
            Vec2(-1, 0),
            Vec2(1, 0),
            Vec2(0, -1),
        ],
        CONFIG.colors.purple,
        "T.png",
    )

    S = FigureParams(  # type: ignore
        [
            Vec2(0, 0),
            Vec2(-1, 0),
            Vec2(0, -1),
            Vec2(1, -1),
        ],
        CONFIG.colors.green,
        "S.png",
    )
    Z = FigureParams(  # type: ignore
        [
            Vec2(0, 0),
            Vec2(1, 0),
            Vec2(0, -1),
            Vec2(-1, -1),
        ],
        CONFIG.colors.red,
        "Z.png",
    )
    J = FigureParams(  # type: ignore
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, 1),
            Vec2(-1, 1),
        ],
        CONFIG.colors.blue,
        "J.png",
    )
    L = FigureParams(  # type: ignore
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, 1),
            Vec2(1, 1),
        ],
        CONFIG.colors.orange,
        "L.png",
    )

    @classmethod
    def random(cls) -> "Figure":
        return random.choice(list(cls))
