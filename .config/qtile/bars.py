from libqtile.bar import Bar
from libqtile.widget import (
    GroupBox,
    WindowCount,
    WindowName,
    Memory,
    CPU,
    Clock,
    Systray,
    Sep,
    Net,
    Volume,
    TextBox
)

from colors import nord
import unicodes

HIGHT = 24

bar1 = Bar(
    [
        Sep(
            linewidth = 0,
            padding = 5,
        ),
        GroupBox(
            disable_drag = True,
            fontsize = 16,
            background = nord['bg-secondary'],
            active = nord["cyan"],
            inactive = nord["inactive"],
            highlight_method = "text",
            this_current_screen_border = nord['yellow'],
            other_current_screen_border = nord['yellow'],
        ),
        unicodes.right_arrow(nord['yellow'], nord['bg-secondary']),
        
        Clock(
            format="%a %d, %H:%M",
            background=nord["yellow"],
            foreground = nord['bg-primary']
        ),
        unicodes.right_arrow(nord['bg-primary'], nord['yellow']),

        WindowName(),
        unicodes.left_arrow(nord['bg-primary'], nord['inactive']),

        Systray(
            icon_size = 21,
            background = nord['inactive'],
        ),
        Sep(
            linewidth = 0,
            padding = 10,
            background = nord['inactive']
        ),

        unicodes.left_arrow(nord['inactive'], nord['green']),
        Memory(
            format = "\uefc5  {MemPercent:.0f}%",
            background = nord['green'],
            foreground = nord['inactive']
        ),
        CPU(
            format = "\uf4bc  {load_percent:.0f}%",
            background = nord["green"],
            foreground = nord["inactive"],
            # padding = 5,
        ),

        unicodes.left_arrow(nord['green'], nord['blue']),
        TextBox(
            text = "",
            background = nord['blue'],
            foreground = nord['bg-primary'],
        ),
        Volume(
            background = nord['blue'],
            foreground = nord['bg-primary'],
            # emoji = True,
            get_volume_command = "amixer get Master | grep -oP '\d+%' | head -1",
            # emoji_list = ["󰝟", "󰕿", "󰖀", "󰕾"],
            # fontsize = 18,
        ),
        
        unicodes.left_arrow(nord['blue'], nord['red']),
        Net(
            background = nord['red'],
            # foreground = nord[], 
            prefix = "k",
            format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
        ),
        Sep(
            linewidth = 0,
            padding = 5,
        ),
    ],
    size = HIGHT,
    background = nord['bg-primary'],
    margin = [0, -5, 0, -5],
)

