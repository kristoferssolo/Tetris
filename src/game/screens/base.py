from abc import ABC, ABCMeta, abstractmethod


class BaseScreen(ABC, metaclass=ABCMeta):
    """Base screen class."""

    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        """Update the screen."""

    @abstractmethod
    def draw(self, *args, **kwargs) -> None:
        """Draw the screen."""

    @abstractmethod
    def run(self, *args, **kwargs) -> None:
        """Run the screen."""


class SceenElement(ABC, metaclass=ABCMeta):
    @abstractmethod
    def _draw_background(self) -> None:
        """Draw the background."""

    @abstractmethod
    def _draw_border(self) -> None:
        """Draw the border."""

    @abstractmethod
    def _initialize_surface(self) -> None:
        """Initialize the surface."""

    @abstractmethod
    def _initialize_rect(self) -> None:
        """Initialize the rectangle."""

    @abstractmethod
    def _update_display_surface(self) -> None:
        """Update the display surface."""


class TextScreen(ABC, metaclass=ABCMeta):
    """Base screen class for text."""

    @abstractmethod
    def _initialize_font(self) -> None:
        """Initialize the font."""

    @abstractmethod
    def _draw_text(self) -> None:
        """Draw the text on the surface."""

    @abstractmethod
    def _display_text(self, *args, **kwargs) -> None:
        """Display the text."""
