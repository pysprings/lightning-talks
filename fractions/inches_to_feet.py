#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick example of using the fractions module to convert inches to fractional feet.

https://docs.python.org/3/library/fractions.html#module-fractions
"""
import sys
import fractions

value = float(sys.argv[1])

feet, inches = divmod(value, 12)
whole_inches, partial_inches = divmod(inches, 1)

if partial_inches:
    fractional_inches = fractions.Fraction(partial_inches).limit_denominator()
    print(f"{value:.2f}\" == {feet:.0f}' {whole_inches:.0f} {fractional_inches}\"")
else:
    print(f"{value:.2f}\" == {feet:.0f}' {whole_inches:.0f}\"")