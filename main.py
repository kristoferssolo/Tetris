#!/usr/bin/env python
import argparse
import sys

from loguru import logger
from utils import BASE_PATH, CONFIG, GameMode

parser = argparse.ArgumentParser(description="Tetris game with AI")
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-d",
    "--debug",
    action="store_true",
    help="Debug",
)

group.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Verbose",
)

parser.add_argument(
    "-g",
    "--graphic",
    action="store_true",
    help="Run app with GUI [Default]",
)


def setup_logger(level: str = "warning") -> None:
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="<green>{time}</green> | <level>{level}</level> | <level>{message}</level>",
        level=level.upper(),
        colorize=True,
    )

    logger.add(
        BASE_PATH / ".logs" / "teris.log",
        format="{time} | {level} | {message}",
        level="DEBUG" if level.upper() == "DEBUG" else "INFO",
        rotation="10 MB",
        compression="zip",
    )


@logger.catch
def run() -> None:
    import game

    logger.debug("Launching the game")
    game.Main(GameMode.PLAYER).run()


def main(args: argparse.ArgumentParser) -> None:
    if args.debug:
        level = "debug"
    elif args.verbose:
        level = "info"
    else:
        level = "warning"

    setup_logger(level)

    run()


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
