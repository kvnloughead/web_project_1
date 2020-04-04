#!/usr/bin/env python3
# Program to automatically populate element folders with their appropriate css files.
# Assumes that elements are written as .block__element
# Unfinished

import shutil
import os
import sys

blocks_dir = sys.argv[1]
css_file = open(sys.argv[2], "r")

# get blocks and elements
blocks = {}
for line in css_file.readlines():
    if line[0] == ".":
        block = line.split("__")[0][1:]
        if block not in blocks:
            blocks[block] = []
        




    

# for root, dirs, files in os.walk(blocks_dir):
#     for dir in dirs:
#         filepath = os.path.join(f"{blocks_dir}/{dir}", f"{dir}.css")
#         f = open(filepath, "w+")
#         f.close()