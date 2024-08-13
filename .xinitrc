# Starting Pipewire & Wireplumber for Audio
/usr/bin/pipewire &
/usr/bin/pipewire-pulse &
/usr/bin/wireplumber &

# IBus for Multi-lingual Typing
ibus-daemon -drx

# Disable beep
xset -b

# Compositor
picom -b

# Wallpaper
nitrogen --restore

# Unclutter - Hide mouse cursor
unclutter --jitter 10 --ignore-scrolling --start-hidden --fork

# Turn numlock on
if [ -x /usr/bin/numlockx ]; then
  /usr/bin/numlockx on
fi

# Start qtile
qtile start
