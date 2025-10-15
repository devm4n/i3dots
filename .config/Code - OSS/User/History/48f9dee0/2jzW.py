import json
import os

home = os.path.expanduser('~')
colors_file = f'{home}/.cache/wal/colors.json'
output_file = f'{home}/.cache/wal/colors-alacritty.toml'

with open(colors_file, 'r') as f:
    colors = json.load(f)['colors']

alacritty_config = f'''[colors.primary]
background = \'{colors[\"color0\"]}\'
foreground = \'{colors[\"color7\"]}\'

[colors.normal]
black = \'{colors[\"color0\"]}\'
red = \'{colors[\"color1\"]}\'
green = \'{colors[\"color2\"]}\'
yellow = \'{colors[\"color3\"]}\'
blue = \'{colors[\"color4\"]}\'
magenta = \'{colors[\"color5\"]}\'
cyan = \'{colors[\"color6\"]}\'
white = \'{colors[\"color7\"]}\'

[colors.bright]
black = \'{colors[\"color8\"]}\'
red = \'{colors[\"color9\"]}\'
green = \'{colors[\"color10\"]}\'
yellow = \'{colors[\"color11\"]}\'
blue = \'{colors[\"color12\"]}\'
magenta = \'{colors[\"color13\"]}\'
cyan = \'{colors[\"color14\"]}\'
white = \'{colors[\"color15\"]}\'

with open(output_file, 'w') as f:
    f.write(alacritty_config)

print(f'Generated {output_file}')
