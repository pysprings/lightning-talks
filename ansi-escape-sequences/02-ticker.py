#!/usr/bin/env python3

import time
from itertools import cycle

ticker_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
spinner = cycle(ticker_frames)

end_time = time.time() + 10

while time.time() < end_time:
    tick = next(spinner)
    print(tick)
    time.sleep(0.5)
