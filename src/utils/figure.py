import random
from enum import Enum
from typing import NamedTuple

from attr import define
from pygame import Vector2 as Vec2

from .colors import TokyoNightNight


class FigureConfig(NamedTuple):
    shape: list[Vec2]
    color: str


class Figure(Enum):
    I = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, -2),
            Vec2(0, 1),
        ],
        TokyoNightNight().cyan,
    )
    O = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(1, 0),
            Vec2(1, -1),
        ],
        TokyoNightNight().yellow,
    )
    T = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(-1, 0),
            Vec2(1, 0),
            Vec2(0, -1),
        ],
        TokyoNightNight().purple,
    )

    S = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(-1, 0),
            Vec2(0, -1),
            Vec2(1, -1),
        ],
        TokyoNightNight().green,
    )
    Z = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(1, 0),
            Vec2(0, -1),
            Vec2(-1, -1),
        ],
        TokyoNightNight().red,
    )
    J = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, 1),
            Vec2(-1, 1),
        ],
        TokyoNightNight().blue,
    )
    L = FigureConfig(
        [
            Vec2(0, 0),
            Vec2(0, -1),
            Vec2(0, 1),
            Vec2(1, 1),
        ],
        TokyoNightNight().orange,
    )

    @staticmethod
    def random() -> "Figure":
        return random.choice(list(Figure))
