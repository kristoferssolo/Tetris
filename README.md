# Tetri
![Tests](https://github.com/kristoferssolo/Tetris/actions/workflows/tests.yml/badge.svg) ![Lint](https://github.com/kristoferssolo/Tetris/actions/workflows/lint.yml/badge.svg)

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Running the game](#running-the-game)
- [Settings](#settings)
  * [General Settings](#general-settings)
  * [Movement Settings](#movement-settings)
  * [Rotation Settings](#rotation-settings)
  * [Action Settings](#action-settings)
  * [Volume Settings](#volume-settings)
    + [Music](#music)
    + [Sound Effects (SFX)](#sound-effects-sfx)
- [Acknowledgments](#acknowledgments)

<!-- tocstop -->

## Overview

Welcome to Tetris, a classic and timeless game implemented in Python using the [Pygame](https://www.pygame.org/) library.

## Prerequisites
Before running the Tetris game, make sure you have the following installed on your system:
- Python (version 3.11 recommended)

## Running the game

1. Clone the repository:
```bash
git clone https://github.com/kristoferssolo/Tetris
```

2. Navigate to the project directory:
```bash
cd Tetris
```

3. Install the required dependencies:
```bash
pip install -e .
```

4. Run the game:
```bash
python main.py
# or
python -m tetris
```

## Settings
The `settings.toml` file is a configuration file for customizing various aspects of the game.

### General Settings
- `pause`: Defines the keys to pause the game. Currently a work in progress.
- `quit`: Defines the key(s) to quit the game.
- `colorscheme`: Specifies the color scheme for the game interface. Options include:
  - `tokyonight-night`
  - `tokyonight-storm`
  - `tokyonight-day`
  - `tokyonight-moon`

### Movement Settings
- `left`: Defines the keys to move the tetromino[^tetromino] left.
- `right`: Defines the keys to move the tetromino right.
- `down`: Defines the keys to accelerate the tetromino's fall.

### Rotation Settings
- `cw (clockwise )`: Defines the keys to rotate the tetromino in a clockwise direction.
- `ccw (counter-clockwise)`: Defines the keys to rotate the tetromino in a counter-clockwise direction.

### Action Settings
- `hold`: Defines the keys to hold the tetromino (WIP[^WIP]).
- `drop`: Defines the keys to instantly drop the tetromino.

### Volume Settings
#### Music
- `enabled`: Indicates whether music is enabled.
- `level`: Specifies the volume level for the music.

#### Sound Effects (SFX)
- `enabled`: Indicates whether sound effects are enabled.
- `level`: Specifies the volume level for the sound effects.


## Acknowledgments
Thanks to [Folke](https://github.com/folke), the creator of [TokyoNight](https://github.com/folke/tokyonight.nvim) color theme.

[^WIP]: Work In Progress.
[^tetromino]: A tetromino is a geometric shape composed of four squares, connected orthogonally (i.e. at the edges and not the corners).
