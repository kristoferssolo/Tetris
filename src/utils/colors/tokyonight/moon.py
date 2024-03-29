from attr import define

from .base import Color


@define
class TokyoNightMoon(Color):
    bg = "#222436"
    bg_dark = "#1e2030"
    bg_float = "#1e2030"
    bg_highlight = "#2f334d"
    bg_popup = "#1e2030"
    bg_search = "#3e68d7"
    bg_sidebar = "#1e2030"
    bg_statusline = "#1e2030"
    bg_visual = "#2d3f76"
    black = "#1b1d2b"
    blue = "#82aaff"
    blue0 = "#3e68d7"
    blue1 = "#65bcff"
    blue2 = "#0db9d7"
    blue5 = "#89ddff"
    blue6 = "#b4f9f8"
    blue7 = "#394b70"
    border = "#1b1d2b"
    border_highlight = "#589ed7"
    comment = "#636da6"
    cyan = "#86e1fc"
    dark3 = "#545c7e"
    dark5 = "#737aa2"
    delta_add = "#305f6f"
    delta_delete = "#6b2e43"
    diff_add = "#273849"
    diff_change = "#252a3f"
    diff_delete = "#3a273a"
    diff_text = "#394b70"
    error = "#c53b53"
    fg = "#c8d3f5"
    fg_dark = "#828bb8"
    fg_float = "#c8d3f5"
    fg_gutter = "#3b4261"
    fg_sidebar = "#828bb8"
    git_add = "#b8db87"
    add_change = "#7ca1f2"
    add_delete = "#e26a75"
    add_ignore = "#545c7e"
    git_signs_add = "#627259"
    git_signs_change = "#485a86"
    git_signs_delete = "#b55a67"
    green = "#c3e88d"
    green1 = "#4fd6be"
    green2 = "#41a6b5"
    hint = "#4fd6be"
    info = "#0db9d7"
    magenta = "#c099ff"
    magenta2 = "#ff007c"
    orange = "#ff966c"
    purple = "#fca7ea"
    red = "#ff757f"
    red1 = "#c53b53"
    teal = "#4fd6be"
    terminal_black = "#444a73"
    warning = "#ffc777"
    yellow = "#ffc777"
