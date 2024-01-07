from pathlib import Path
from typing import Optional

import toml

from .config import CONFIG, Config
from .log import log


def save_settings(settings: Config, file_path: Path) -> None:
    with open(file_path, "w") as file:
        toml.dump(settings, file)


def read_settings(file_path: Path) -> Optional[dict[str, str]]:
    """
    Read and parse a TOML file and return the content as a dictionary.

    Args:
        file_path: The path to the TOML file.

    Returns:
        dict: The parsed content of the TOML file.
    """
    try:
        with open(file_path, "r") as file:
            return toml.load(file)
    except FileNotFoundError:
        log.error(f"Error: The file '{file_path}' does not exist.")
        return None
    except toml.TomlDecodeError as e:
        log.error(f"rror decoding TOML file: {e}")
        return None
