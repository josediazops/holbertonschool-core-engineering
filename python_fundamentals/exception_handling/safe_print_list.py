#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    number_printed = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            number_printed += 1
        except IndexError:
            break
    print()
    return number_printed
