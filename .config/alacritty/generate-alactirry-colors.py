import json
import os

home = os.path.expanduser('~')
colors_file = home + '/.cache/wal/colors.json'
output_file = home + '/.cache/wal/colors-alacritty.toml'

with open(colors_file, 'r') as f:
    colors = json.load(f)['colors']

alacritty_config = '[colors.primary]\n'
alacritty_config += 'background = "' + colors['color0'] + '"\n'
alacritty_config += 'foreground = "' + colors['color7'] + '"\n\n'

alacritty_config += '[colors.normal]\n'
alacritty_config += 'black = "' + colors['color0'] + '"\n'
alacritty_config += 'red = "' + colors['color1'] + '"\n'
alacritty_config += 'green = "' + colors['color2'] + '"\n'
alacritty_config += 'yellow = "' + colors['color3'] + '"\n'
alacritty_config += 'blue = "' + colors['color4'] + '"\n'
alacritty_config += 'magenta = "' + colors['color5'] + '"\n'
alacritty_config += 'cyan = "' + colors['color6'] + '"\n'
alacritty_config += 'white = "' + colors['color7'] + '"\n\n'

alacritty_config += '[colors.bright]\n'
alacritty_config += 'black = "' + colors['color8'] + '"\n'
alacritty_config += 'red = "' + colors['color9'] + '"\n'
alacritty_config += 'green = "' + colors['color10'] + '"\n'
alacritty_config += 'yellow = "' + colors['color11'] + '"\n'
alacritty_config += 'blue = "' + colors['color12'] + '"\n'
alacritty_config += 'magenta = "' + colors['color13'] + '"\n'
alacritty_config += 'cyan = "' + colors['color14'] + '"\n'
alacritty_config += 'white = "' + colors['color15'] + '"\n'

with open(output_file, 'w') as f:
    f.write(alacritty_config)

print('Generated ' + output_file)