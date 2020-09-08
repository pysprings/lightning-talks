#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script speeds up the slow way with a potentially much faster way.
"""

import time
from multiprocessing import Pool


def format_timespan(seconds: float) -> str:
    """Formats the number of seconds in h:m:s"""
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{int(hours):d}h:{int(minutes):02d}m:{int(seconds)}s"


def main(count):
    for _ in range(count):
        time.sleep(1)

    print("done with loop")


if __name__ == "__main__":
    start_time = time.time()

    counts = [5, 5, 5]
    with Pool(5) as p:
        p.map(main, counts)

    end_time = time.time()

    print(f"Total compute time: {format_timespan(end_time-start_time)}")
