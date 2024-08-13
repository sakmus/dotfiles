from libqtile.widget.textbox import TextBox


def right_angle(bg, fg):
    return TextBox(
        text = "\ue0bc",
        padding = 0,
        fontsize = 30,
        foreground = fg,
        background = bg
        )


def left_angle(bg, fg):
    return TextBox(
        text = "\ue0be",
        padding = 0,
        fontsize = 30,
        foreground = fg,
        background = bg
        )

def left_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=25,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=35,
        background=bg_color,
        foreground=fg_color)