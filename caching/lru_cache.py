#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple script showing built-in Python caching.
"""
import time
from functools import lru_cache


@lru_cache(maxsize=128)
def calc_pi(number_of_calculations: int) -> float:
    """Keep approximating Pi for some number of times."""
    pi = 0

    for i in range(0, number_of_calculations):
        pi += (4.0 * (-1) ** i) / (2 * i + 1)

    return pi


if __name__ == "__main__":
    digits = 5_000_000  # Something large enough to measure

    # The first time we calculate Pi, it takes a while:
    t_start = time.time()
    calc_pi(digits)
    t_end = time.time()
    print(
        f"The first calculation of {digits:_} digits took {t_end-t_start:.2f} seconds"
    )

    # All subsequent calls won't take "any" time.
    t_start = time.time()
    calc_pi(digits)
    t_end = time.time()
    print(f"The next calculation took {t_end-t_start:.2f} seconds")

    t_start = time.time()
    calc_pi(digits)
    t_end = time.time()
    print(f"The next calculation took {t_end-t_start:.2f} seconds")

    t_start = time.time()
    calc_pi(digits)
    t_end = time.time()
    print(f"The next calculation took {t_end-t_start:.2f} seconds")

    # We'll have to wait again if we change the input.
    t_start = time.time()
    calc_pi(digits * 2)
    t_end = time.time()
    print(f"Calculation of {digits * 2:_} digits took {t_end-t_start:.2f} seconds")
