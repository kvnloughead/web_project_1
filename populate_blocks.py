#!/usr/bin/env python3
# Program to automatically populate block folders with their appropriate css files.

import shutil
import os
import sys

d = sys.argv[1]

for root, dirs, files in os.walk(d):
    for dir in dirs:
        filepath = os.path.join(f"{d}/{dir}", f"{dir}.css")
        f = open(filepath, "w+")
        f.close()