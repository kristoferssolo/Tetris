from typing import Callable, NamedTuple, Optional

import pygame
from attrs import define, field


@define
class Timer:
    duration: int = field(converter=int)
    repeated: bool = field(default=False)
    func: Optional[Callable[[None], None]] = field(default=None)
    start_time: int = 0
    active: bool = False

    def activate(self) -> None:
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self) -> None:
        self.active = False
        self.start_time = 0

    def update(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration and self.active:
            if self.func and self.start_time:
                self.func()

            self.deactivate()

            if self.repeated:
                self.activate()


class Timers(NamedTuple):
    vertical: Timer
    horizontal: Timer
