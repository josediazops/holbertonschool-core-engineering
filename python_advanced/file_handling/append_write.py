#!/usr/bin/env python3
"""Create a function that appends a string"""


def append_write(filename="", text=""):
    """Write a string at the end of a text file and return number"""
    # open the file named by filename in append mode, encoding utf-8
    with open(filename, "a", encoding="utf-8") as f:
        # write text at the end of the file and keep the count
        text = f.write(text)
    return text
