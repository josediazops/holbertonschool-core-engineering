#!/usr/bin/env python3

def uppercase(value):
    result = ""

    for char in str(value):
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char

    print(result)
