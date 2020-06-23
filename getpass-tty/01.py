#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script that only uses the getpass method.
"""

from getpass import getpass

password = getpass("Enter your password: ")
print(f"you entered: {password}")