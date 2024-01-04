#!/usr/bin/env python
import argparse

from loguru import logger
from utils import BASE_PATH, CONFIG


def pos_int(string: str) -> int:
    ivalue = int(string)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{ivalue} is not a positive integer")
    return ivalue


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
    "-t",
    "--train",
    type=pos_int,
    nargs=2,
    metavar=("generations", "parallels"),
    help="Trains the AI",
)

parser.add_argument(
    "-g",
    "--graphic",
    action="store_true",
    help="Run app with GUI [Default]",
)

logger.add(
    BASE_PATH / ".logs" / "teris.log",
    format="{time} | {level} | {message}",
    level="WARNING",
    rotation="10 MB",
    compression="zip",
)


@logger.catch
def main(args: argparse.ArgumentParser) -> None:
    if args.debug:
        CONFIG.log_level = "debug"
    elif args.verbose:
        CONFIG.log_level = "info"

    import ai
    import game

    if args.train is not None:
        ai.log.debug("Training the AI")
        ai.train(*args.train)
    else:
        game.log.debug("Running the game")
        game.Main().run()


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
