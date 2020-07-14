#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script returns the total length of a number of measurements.
"""

import re
from fractions import Fraction


PATTERN = r"""
    (?P<feet>[0-9]+)'\s*
    (?P<inches>[0-9\s\/]+")?
"""

INCHES = r"""
    (?P<inches>[0-9]+)\s*
    ((?P<fraction>[0-9/]+)")?
"""


def parse(value):
    """Parses a value and return the total inches as a float."""
    feet = 0
    whole_inches = 0
    fractional_inches = Fraction(0, 1)

    match = re.search(PATTERN, value, re.VERBOSE)
    feet = int(match.group("feet") or 0)

    match = re.search(INCHES, match.groupdict().get("inches") or "", re.VERBOSE)
    if match:
        whole_inches = int(match.group("inches"))
        if match.group("fraction"):
            numerator, denominator = match.group("fraction").split("/")
            fractional_inches = Fraction(int(numerator), int(denominator))

    return feet * 12.0 + float(whole_inches + fractional_inches)


def calculate(values):
    """
    Sums up all measurements and returns a simplified string in `{feet}' {inches}"`
    """
    total_inches = sum(values)
    feet, inches = divmod(total_inches, 12)
    whole_inches, partial_inches = divmod(inches, 1)

    if partial_inches:
        fractional_inches = Fraction(partial_inches).limit_denominator()
        return f"{feet:.0f}' {whole_inches:.0f} {fractional_inches}\""
    else:
        return f"{feet:.0f}' {whole_inches:.0f}\""


def main():
    values = []

    print("Enter length values like: 10' 6 3/4\"")
    print()

    value = input("Enter the first length [enter to quit]: ")
    while value:
        values.append(value)
        value = input("Enter the next length [enter to quit]: ")

    # Convert all values into fractions
    parsed_values = []
    for value in values:
        parsed_values.append(parse(value))

    total_length = calculate(parsed_values)

    print()
    print(f"{' + '.join(values)} == {total_length}")


if __name__ == "__main__":
    main()
