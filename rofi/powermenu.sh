#!/bin/bash

options="󰐥   Shutdown\n   Reboot\n󰤄   Suspend\n   Lock\n󰍃   Logout"
chosen=$(echo -e "$options" | rofi -dmenu -i -p "Power Menu" -theme ~/.config/rofi/powermenu.rasi)

# Detect current session
if [ "$XDG_CURRENT_DESKTOP" = "Hyprland" ] || [ -n "$HYPRLAND_INSTANCE_SIGNATURE" ]; then
    LOCK_CMD="hyprlock"
    LOGOUT_CMD="hyprctl dispatch exit"
elif [ -n "$I3SOCK" ] || [ "$XDG_CURRENT_DESKTOP" = "i3" ]; then
    LOCK_CMD="i3lock"
    LOGOUT_CMD="i3-msg exit"
else
    LOCK_CMD="xdg-screensaver lock"
    LOGOUT_CMD="loginctl terminate-session $XDG_SESSION_ID"
fi

case $chosen in
    "󰐥   Shutdown")
        systemctl poweroff
        ;;
    "   Reboot")
        systemctl reboot
        ;;
    "󰤄   Suspend")
        systemctl suspend
        ;;
    "   Lock")
        $LOCK_CMD
        ;;
    "󰍃   Logout")
        $LOGOUT_CMD
        ;;
esac
