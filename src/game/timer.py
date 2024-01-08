from typing import TYPE_CHECKING

import pygame
from attrs import define, field

if TYPE_CHECKING:
    from typing import Any, Callable, NamedTuple, Optional


@define
class Timer:
    """
    Timer class for managing timed events.

    Args:
        duration: Duration of the timer in milliseconds.
        repeated: Whether the timer should repeat after each completion.
        func: Callback function to execute when the timer completes.

    Attributes:
        duration: Duration of the timer in milliseconds.
        repeated: Whether the timer should repeat after each completion.
        func: Callback function to execute when the timer completes.
        start_time: Time when the timer was last activated.
        active: Indicates whether the timer is currently active.
    """

    duration: float = field(converter=float)
    repeated: bool = field(default=False)
    func: Optional[Callable[[], Any]] = field(default=None)
    start_time: int = 0
    active: bool = False

    def activate(self) -> None:
        """Activates the timer, setting the start time to the current time."""
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self) -> None:
        """Deactivates the timer, resetting the start time to 0."""
        self.active = False
        self.start_time = 0

    def update(self) -> None:
        """
        Updates the timer, checking if it has completed its duration.

        If completed, executes the callback function (if provided) and either deactivates or reactivates the timer.
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration and self.active:
            if self.func and self.start_time:
                self.func()

            self.deactivate()

            if self.repeated:
                self.activate()


class Timers(NamedTuple):
    """
    NamedTuple for grouping different timers.

    Args and Attributes:
        vertical: Timer for vertical movement.
        horizontal: Timer for horizontal movement.
        rotation: Timer for rotation.
        drop: Timer for dropping.
    """

    vertical: Timer
    horizontal: Timer
    rotation: Timer
    drop: Timer
