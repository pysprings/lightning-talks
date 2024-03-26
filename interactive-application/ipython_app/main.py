#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys

from IPython import embed


USAGE = """A simple application to show how to use IPython.embed to add
interactivity to your application."""


def parse_args(args: list[str] = sys.argv[1:]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(usage=USAGE)
    parser.add_argument(
        "-i", "--interact", help="Enter an interactive prompt", action="store_true"
    )
    return parser.parse_args(args)


def is_prime(num: int) -> bool:
    """This function return True if the integer is a prime number, False otherwise."""
    if int(num) == 1:
        return False

    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True


def main():
    args = parse_args()

    if args.interact:
        embed(
            header="Welcome to app's interactive console!\nTry out the following functions:\nis_prime",
            colors="neutral",
        )
    else:
        print(is_prime(10))


if __name__ == "__main__":
    main()
