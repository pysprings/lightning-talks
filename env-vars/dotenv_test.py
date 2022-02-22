#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
load_dotenv()

PASSWORD = os.getenv("PASSWORD")
print(f"the password is '{PASSWORD}'")
