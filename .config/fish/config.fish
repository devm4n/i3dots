if status is-interactive
    # Commands to run in interactive sessions can go here
end
wal -R -q
python3 ~/generate-alacritty-colors.py 2>/dev/null &
set -g fish_greeting ""
