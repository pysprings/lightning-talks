#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script that allows `echo`
"""

import sys
from getpass import getpass

# File descriptors (e.g. the result of `open()`, stdin/stdout/stderr, etc)
# have an `isatty()` method that returns True if a TTY-like device is attached
# to the descriptor.  `echo` is *NOT* a TTY-like device.
if sys.stdin.isatty():
    password = getpass("Enter your password: ")
else:
    password = sys.stdin.readline().rstrip()

print(f"you entered: {password}")