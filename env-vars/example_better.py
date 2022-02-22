#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
username = os.getenv("USERNAME")

if not username:
    raise ValueError("No user defined")
