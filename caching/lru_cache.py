#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple script showing built-in Python caching.
"""
import time
from contextlib import contextmanager
from functools import lru_cache


@contextmanager
def timeit(calculations):
    """A simple context manager to print the time it takes to call a function."""
    t_start = time.time()
    yield
    t_end = time.time()
    print(f"{calculations:_} calculations took {t_end-t_start:.2f} seconds")


@lru_cache(maxsize=2)
def calc_pi(number_of_calculations: int) -> float:
    """Keep approximating Pi some number of times."""
    pi = 0

    for i in range(0, number_of_calculations):
        pi += (4.0 * (-1) ** i) / (2 * i + 1)

    return pi


def test_one():
    """
    Call the `calc_pi` function with the same input multiple times.

    The inputs to `calc_pi` are all the same.  The results will be cached, so
    only the first call will take measureable time.
    """
    calculations = 5_000_000  # High enough to take some time

    with timeit(calculations):
        calc_pi(calculations)

    with timeit(calculations):
        calc_pi(calculations)

    with timeit(calculations):
        calc_pi(calculations)


def test_two():
    """
    Call the `calc_pi` function with two different inputs.

    The first calls for each input will take time, but subsequent calls will not.
    """
    calculations = 5_000_000  # High enough to take some time

    # Call the function with the same input 3 times
    with timeit(calculations):
        calc_pi(calculations)
    with timeit(calculations):
        calc_pi(calculations)
    with timeit(calculations):
        calc_pi(calculations)

    # Now change the input.  Only the first call should take time.
    calculations = 6_000_000

    with timeit(calculations):
        calc_pi(calculations)
    with timeit(calculations):
        calc_pi(calculations)
    with timeit(calculations):
        calc_pi(calculations)


def test_three():
    """
    Mix up the calculations to go above `maxsize`.

    This shows that previously-cached returns can be removed from cache automatically
    to prevent the cache from growing indefinitely.
    """
    with timeit(5_000_000):
        calc_pi(5_000_000)
    with timeit(5_000_000):
        calc_pi(5_000_000)

    with timeit(6_000_000):
        calc_pi(6_000_000)
    with timeit(6_000_000):
        calc_pi(6_000_000)

    with timeit(7_000_000):
        calc_pi(7_000_000)
    with timeit(7_000_000):
        calc_pi(7_000_000)

    # The first calculation should have been removed.  Call the same function
    # again, but this time the result will not be cached because we told `lru_cache`
    # to only cache 2 returns.
    with timeit(5_000_000):
        calc_pi(5_000_000)

    # However, 7_000_000 should _still_ be cached since it was just called.
    with timeit(7_000_000):
        calc_pi(7_000_000)


if __name__ == "__main__":
    test_one()
    # test_two()
    # test_three()
