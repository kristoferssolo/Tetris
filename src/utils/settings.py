from pathlib import Path
from typing import Any

import toml
from loguru import logger

from .path import BASE_PATH


def save_settings(settings: dict[str, Any], file_path: Path) -> None:
    """
    Save the settings to a TOML file.

    Args:
        settings: The settings to save.
        file_path: The path to the TOML file.
    """
    with open(file_path, "w") as file:
        toml.dump(settings, file)


def read_settings(
    file_path: Path = BASE_PATH / "settings.toml",
) -> dict[str, Any]:
    """
    Read and parse a TOML file and return the content as a dictionary.

    Args:
        file_path: The path to the TOML file.

    Returns:
        dict: The parsed content of the TOML file.
    """
    try:
        with open(file_path, "r") as file:
            return dict(toml.load(file))
    except FileNotFoundError:
        logger.error(f"Error: The file '{file_path}' does not exist.")
        return {}
    except toml.TomlDecodeError as e:
        logger.error(f"rror decoding TOML file: {e}")
        return {}
