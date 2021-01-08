#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Supporting functions for sample purposes.
"""

import math
import secrets
import string
from typing import Iterable, Tuple

SECONDS_PER_YEAR = 3.154e7
SECONDS_PER_MONTH = 2.628e6
SECONDS_PER_WEEK = 604799.33719968
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600


def get_time_format(seconds: int) -> str:
    """Function to format a number of seconds into something more readable."""
    if seconds >= SECONDS_PER_YEAR:
        return f"{seconds / SECONDS_PER_YEAR:,.2f} years"
    elif seconds >= SECONDS_PER_MONTH:
        return f"{seconds / SECONDS_PER_MONTH:,.2f} months"
    elif seconds >= SECONDS_PER_WEEK:
        return f"{seconds / SECONDS_PER_WEEK:,.2f} weeks"
    elif seconds >= SECONDS_PER_DAY:
        return f"{seconds / SECONDS_PER_DAY:,.2f} days"
    elif seconds >= SECONDS_PER_HOUR:
        return f"{seconds / SECONDS_PER_HOUR:,.2f} hours"
    else:
        return f"{seconds:.2f} seconds"


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


def calulate_entropy_crack_time(
    len_of_password: int,
    len_of_choices: int,
    guesses_per_second: int = 1_000_000_000_000,
):
    max_guesses = number_of_guesses(len_of_password, len_of_choices)
    average_guesses = max_guesses // 2
    entropy = math.log2(max_guesses)
    seconds_to_guess_on_average = average_guesses // guesses_per_second

    return (entropy, seconds_to_guess_on_average)


def number_of_guesses(len_of_password: int, len_of_choices: int):
    return len_of_choices ** len_of_password


def seconds_to_crack(
    len_of_password: int,
    len_of_choices: int,
    guesses_per_second: int = 1_000_000_000_000,
):
    """Approximate the time it would take to crack a password of a given entropy."""
    number_of_guesses = len_of_choices ** len_of_password
    average_guesses = float(number_of_guesses) / 2.0
    return average_guesses / guesses_per_second


def display_stats(choices: Iterable, len_of_password: int):
    """Just a small example of how long it might take to guess a password."""
    len_of_choices = len(choices)
    number_of_guesses = len_of_choices ** len_of_password
    entropy = math.log2(number_of_guesses)
    average_guesses = (number_of_guesses) // 2
    guesses_per_second = 1_000_000_000_000  # 1 trillion (most I've seen is 350B)
    seconds_to_guess_on_average = average_guesses // guesses_per_second
    print(
        f"It would take approx {get_time_format(seconds_to_guess_on_average)} "
        f"to guess that password.  "
        f"entropy = {entropy:.2f}"
    )


def define_ranges() -> Tuple[str, str]:
    """Define some character ranges from which to create passwords."""
    shell_no_need_escape = ",._+:@%/-}]"
    no_lookalikes = "".join(
        [
            c
            for c in (string.ascii_letters + string.digits)
            if c.lower() not in ["1", "l", "i", "o", "0"]
        ]
    )

    return (
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


def sort_ranges(ranges: Tuple[Tuple[str, str]]) -> Tuple[str, str]:
    """Custom sorting function based on the range's entropy"""
    return sorted(ranges, key=lambda x: entropy(len(x[1]), 10), reverse=True)


def generate_passwords(count: int = 5, length: int = 24, character_ranges=None):
    character_ranges = character_ranges or define_ranges()
    for description, choices in sort_ranges(character_ranges):
        e = entropy(s=len(choices), l=length)
        print(f"---- {description} (entropy: {e:.2f}):")
        for _ in range(count):
            characters = []
            for _ in range(length):
                characters.append(secrets.choice(choices))

            password = "".join(characters)
            print(password)


def get_xy(choices, password_lengths, guesses_per_second=1e12):
    """Return values for plotting on a Y axis based on the choices."""
    # y_values will be a list of (entropy, seconds) for each length
    y_values = [
        calulate_entropy_crack_time(passlen, len(choices), guesses_per_second)
        for passlen in password_lengths
    ]
    y_entropy = [x[0] for x in y_values]
    y_seconds = [x[1] for x in y_values]

    return (y_entropy, y_seconds)


def average_time(len_of_choices, len_of_password):
    """Just a small example of how long it might take to guess a password."""
    number_of_guesses = len_of_choices ** len_of_password
    entropy = math.log2(number_of_guesses)
    average_guesses = (number_of_guesses) / 2
    guesses_per_second = 1_000_000_000_000  # 1 trillion (most I've seen is 350B)
    seconds_to_guess_on_average = average_guesses / guesses_per_second
    return seconds_to_guess_on_average
