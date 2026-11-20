#!/usr/bin/env python3


def read_file(filename=""):
    # open the file in read mode using the with statement, encoding utf-8
    with open(filename, "r", encoding="utf-8") as f:
        # read the entire content of the file into a variable
        text = f.read()
    # print that variable, adding nothing at the end
    print(text, end="")
