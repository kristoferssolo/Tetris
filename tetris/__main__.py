#!/usr/bin/env python
import argparse
import sys

from loguru import logger

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

parser.add_argument(
    "-t",
    "--train",
    action="store_true",
    help="Train AI",
)


def setup_logger(level: str = "warning") -> None:
    from utils import BASE_PATH

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
    from utils import GameMode

    logger.debug("Launching the game")
    game.Main(GameMode.PLAYER).run()


def main(args) -> None:
    if args.debug:  # type: ignore
        level = "debug"
    elif args.verbose:  # type: ignore
        level = "info"
    else:
        level = "warning"
    setup_logger(level)

    if args.train:  # type: ignore
        import ai

        ai.train()
    else:
        run()


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)  # type: ignore
