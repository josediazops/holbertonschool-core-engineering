#!/usr/bin/env python3
"""Create a tool to write inside the file"""


def write_file(filename="", text=""):
    """writes the content inside the filename and print it to stdout"""
    # open the file named by filename in read mode, encoding utf-8
    with open(filename, "w", encoding="utf-8")as f:
        # write text to the file and keep the number of characters
        text = f.write(text)
    # give that number back to the caller
    return text
