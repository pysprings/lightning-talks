#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is an example of what _not_ to do.

What happens when we add another environment?  This is not scalable.
Maybe it's fine in this example, since it's very short, but imagine if there
were lots of other places modify this list.
"""
import os

run_env = os.getenv("RUN_ENV")

if run_env == "DEV":
    username = "development-user"
elif run_env == "STAGING":
    username = "stage-user"
elif run_env == "PROD":
    username = "production-user"
else:
    raise ValueError("No user defined")
