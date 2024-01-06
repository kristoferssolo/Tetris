from abc import ABC, ABCMeta, abstractmethod
from typing import Callable, Optional

import pygame


class BaseButton(ABC, metaclass=ABCMeta):
    """Base button class."""

    def __init__(self, text: str, action: Optional[Callable[[], None]]) -> None:
        self.action = action
        self.text = text

    @abstractmethod
    def on_click(self) -> None:
        """Handle click event."""

    @abstractmethod
    def on_hover(self, event: pygame.Event) -> None:
        """Handle hover event."""
