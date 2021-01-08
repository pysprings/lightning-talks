#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates random passwords and writes them to stdout.
"""

import argparse
import math
import secrets
import string
import sys


def get_args(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Create some random passwords")
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        help="length of each password to generate; default: 32",
        default=32,
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        help="number of passwords to generate for each range; default: 5",
        default=5,
    )

    return parser.parse_args(args)


def entropy(s: int, l: int):
    """
    Attempts to guess the entropy of a password based on the size of the pool
    of unique characters and the length of the password.

    The calculation is the theoretical maximum entropy.

    https://generatepasswords.org/how-to-calculate-entropy/
    """
    # L = Password Length; Number of symbols in the password
    # S = Size of the pool of unique possible symbols (character set).
    # Number of Possible Combinations = S**L
    # Entropy = log2(Number of Possible Combinations)
    return math.log2(s ** l)


def main():
    args = get_args()

    shell_no_need_escape = ",._+:@%/-}]"
    no_lookalikes = [
        c
        for c in (string.ascii_letters + string.digits)
        if c.lower() not in ["1", "l", "i", "o", "0"]
    ]

    ranges = (
        (
            "letters, numbers, and puncuation",
            string.ascii_letters + string.digits + string.punctuation,
        ),
        (
            "letters, numbers, and shell-safe punctuation",
            string.ascii_letters + string.digits + shell_no_need_escape,
        ),
        ("letters and numbers", string.ascii_letters + string.digits),
        ("lowercase letters, and numbers", string.ascii_lowercase + string.digits),
        ("letters and numbers, with 'look alikes' removed", no_lookalikes),
        ("lowercase hex digits", "abcdef0123456789"),
    )

    # Sort all of the ranges by their theoretical max entropy.
    for description, choices in sorted(
        ranges, key=lambda x: entropy(len(x[1]), args.length), reverse=True
    ):
        e = entropy(s=len(choices), l=args.length)
        print(f"---- {description} (entropy: {e:.2f}):")
        for _ in range(args.count):
            characters = []
            for _ in range(args.length):
                characters.append(secrets.choice(choices))

            password = "".join(characters)
            print(password)


if __name__ == "__main__":
    main()
