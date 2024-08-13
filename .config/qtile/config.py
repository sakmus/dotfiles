
import os
from libqtile import layout, qtile
from libqtile.layout.bsp import Bsp
from libqtile.layout.floating import Floating
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from colors import nord
import unicodes
import bars

mod = "mod4"
terminal = "alacritty"
fileManager = "nemo"
browser = "firefox"

keys = [

    # Launch Applications
    Key([mod], "e", lazy.spawn(fileManager), desc="Launch default file manager"),
    Key([mod], "w", lazy.spawn(browser), desc="Launch default web browser"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod, "shift"], "f", lazy.spawn("firefox"), desc="Launch Firefox web browser"),
    Key([mod, "shift"], "v", lazy.spawn("codium"), desc="Launch VS Codium"),
    Key([mod, "shift"], "d", lazy.spawn("discord"), desc="Launch Discord app"),
    Key([mod, "shift"], "b", lazy.spawn("brave"), desc="Launch Brave browser"),

    # Rofi
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Rofi application launcher"),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show run"), desc="Rofi command launcher"),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window"), desc="Rofi window selector"),

    # Screenshot
    Key([mod, "shift"], "s", lazy.spawn("scrot -s -e 'xclip -selection clipboard -t image/png < $f'"), desc="Selective screenshot"),
    Key([mod], "Print", lazy.spawn("scrot -e 'xclip -selection clipboard -t image/png -i $f'"), desc="Fullscreen screenshot"),
  
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [
    Group('1', label="", matches=[Match(role="browser")], layout="bsp"),
    Group('2', label="", matches=[Match(wm_class="vscodium")], layout="bsp"),
    Group('3', label="", layout="bsp"),
    Group('4', label="", layout="bsp"),
    Group('5', label="", layout="bsp"),
]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    Bsp(
        border_normal = nord["bg-secondary"],
        border_focus = nord["fg"],
        border_width = 4,
        border_on_single = True,
        margin = 10,
        margin_on_single = 10,
    )
]

floating_layout = layout.Floating(
    border_normal = nord["bg-secondary"],
    border_focus = nord["fg"],
    border_width = 4,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="pavucontrol")
    ]
)

widget_defaults = dict(
    font="JetBrains Mono NL",
    fontsize=14,
    padding=10,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top = bars.bar2
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
