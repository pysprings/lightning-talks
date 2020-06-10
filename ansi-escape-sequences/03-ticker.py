#!/usr/bin/env python3

import time
from itertools import cycle

ticker_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
ansi_home = chr(27) + "[H"
ansi_clear = chr(27) + "[2J"

spinner = cycle(ticker_frames)

end_time = time.time() + 10

# Clear the screen
print(ansi_clear)

# Move the cursor to the top-left
print(ansi_home)

while time.time() < end_time:
    tick = next(spinner)
    print(tick, end='', flush=True)
    print(ansi_home)
    time.sleep(0.5)
