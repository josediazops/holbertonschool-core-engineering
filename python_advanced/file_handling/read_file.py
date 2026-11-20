#!/usr/bin/env python3
"""Tools to read a file"""


def read_file(filename=""):
    """Read the content of the filename and print it to stdout"""
    # open the file in read mode using the with statement, encoding utf-8
    with open(filename, "r", encoding="utf-8") as f:
        # read the entire content of the file into a variable
        text = f.read()
    # print that variable, adding nothing at the end
    print(text, end="")
