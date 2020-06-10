#!/usr/bin/env python3

import sys
import time
from random import choice
from itertools import cycle

ticker_frames = (
    ("⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"),
    ("⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"),
    ("▏", "▎", "▍", "▌", "▋", "▊", "▉", "▊", "▋", "▌", "▍", "▎"),
    ("⬆️ ", "↗️ ", "➡️ ", "↘️ ", "⬇️ ", "↙️ ", "⬅️ ", "↖️ "),
    ("[    ]", "[=   ]", "[==  ]", "[=== ]", "[ ===]", "[  ==]", "[   =]", "[    ]", "[   =]", "[  ==]", "[ ===]", "[====]", "[=== ]", "[==  ]", "[=   ]"),
    ("∙∙∙", "●∙∙", "∙●∙", "∙∙●", "∙∙∙"),
)
spinner = cycle(choice(ticker_frames))

ansi_home = chr(27) + "[H"
ansi_clear = chr(27) + "[2J"
ansi_fg_green = chr(27) + "[32m"
ansi_reset_format = chr(27) + "[0m"

end_time = time.time() + 10

# Clear the screen
print(ansi_clear)

# Move the cursor to the top-left
print(ansi_home)

while time.time() < end_time:
    tick = next(spinner)

    # move the cursor to the start
    print(chr(27) + "[1;0H")

    # print the tick
    print(ansi_fg_green, tick, ansi_reset_format, end="", flush=True)

    # Move the cursor out of the way (looks better)
    print(chr(27) + "[2;0H")

    time.sleep(0.2)
