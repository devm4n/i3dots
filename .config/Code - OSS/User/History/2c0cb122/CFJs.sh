#!/bin/bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch Polybar, using default config location ~/.config/polybar/config
# You can specify a different config file with -c /path/to/config
polybar mybar &
# polybar another_bar & # Uncomment to launch another bar if defined in config

echo "Polybar launched..."