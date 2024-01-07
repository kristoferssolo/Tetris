from .tokyonight import TokyoNightDay, TokyoNightMoon, TokyoNightNight, TokyoNightStorm

COLOR_DICT = {
    "tokyonight-day": TokyoNightDay,
    "tokyonight-moon": TokyoNightMoon,
    "tokyonight-night": TokyoNightNight,
    "tokyonight-storm": TokyoNightStorm,
}

__all__ = [
    "TokyoNightMoon",
    "TokyoNightDay",
    "TokyoNightNight",
    "TokyoNightStorm",
    "COLOR_DICT",
]
