from abc import ABC, ABCMeta

from attrs import define


class Color(ABC, metaclass=ABCMeta):
    bg: str
    bg_dark: str
    bg_float: str
    bg_highlight: str
    bg_popup: str
    bg_search: str
    bg_sidebar: str
    bg_statusline: str
    bg_visual: str
    black: str
    blue: str
    blue0: str
    blue1: str
    blue2: str
    blue5: str
    blue6: str
    blue7: str
    border: str
    border_highlight: str
    comment: str
    cyan: str
    dark3: str
    dark5: str
    delta_add: str
    delta_delete: str
    diff_add: str
    diff_change: str
    diff_delete: str
    diff_text: str
    error: str
    fg: str
    fg_dark: str
    fg_float: str
    fg_gutter: str
    fg_sidebar: str
    git_add: str
    git_change: str
    git_delete: str
    git_ignore: str
    git_signs_add: str
    git_signs_change: str
    git_signs_delete: str
    green: str
    green1: str
    green2: str
    hint: str
    info: str
    magenta: str
    magenta2: str
    orange: str
    purple: str
    red: str
    red1: str
    teal: str
    terminal_black: str
    warning: str
    yellow: str