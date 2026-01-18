#!/usr/bin/python3
"""Import add function from add_0.py and use it"""

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
