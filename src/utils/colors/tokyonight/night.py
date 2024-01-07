from attr import define

from .base import Color


@define
class TokyoNightNight(Color):
    bg = "#1a1b26"
    bg_dark = "#16161e"
    bg_float = "#16161e"
    bg_highlight = "#292e42"
    bg_popup = "#16161e"
    bg_search = "#3d59a1"
    bg_sidebar = "#16161e"
    bg_statusline = "#16161e"
    bg_visual = "#283457"
    black = "#15161e"
    blue = "#7aa2f7"
    blue0 = "#3d59a1"
    blue1 = "#2ac3de"
    blue2 = "#0db9d7"
    blue5 = "#89ddff"
    blue6 = "#b4f9f8"
    blue7 = "#394b70"
    border = "#15161e"
    border_highlight = "#27a1b9"
    comment = "#565f89"
    cyan = "#7dcfff"
    dark3 = "#545c7e"
    dark5 = "#737aa2"
    delta_add = "#2c5a66"
    delta_delete = "#713137"
    diff_add = "#20303b"
    diff_change = "#1f2231"
    diff_delete = "#37222c"
    diff_text = "#394b70"
    error = "#db4b4b"
    fg = "#c0caf5"
    fg_dark = "#a9b1d6"
    fg_float = "#c0caf5"
    fg_gutter = "#3b4261"
    fg_sidebar = "#a9b1d6"
    git_add = "#449dab"
    git_change = "#6183bb"
    git_delete = "#914c54"
    git_ignore = "#545c7e"
    git_signs_add = "#266d6a"
    git_signs_change = "#536c9e"
    git_signs_delete = "#b2555b"
    green = "#9ece6a"
    green1 = "#73daca"
    green2 = "#41a6b5"
    hint = "#1abc9c"
    info = "#0db9d7"
    magenta = "#bb9af7"
    magenta2 = "#ff007c"
    orange = "#ff9e64"
    purple = "#9d7cd8"
    red = "#f7768e"
    red1 = "#db4b4b"
    teal = "#1abc9c"
    terminal_black = "#414868"
    warning = "#e0af68"
    yellow = "#e0af68"
