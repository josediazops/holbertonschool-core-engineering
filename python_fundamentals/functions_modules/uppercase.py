#!/usr/bin/env python3

def uppercase(value):
    for char in str(value):
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)

        print("{:c}".format(ord(char)), end="")
    print()
