#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample usage:
python n-queens.py -n 9
"""


import argparse
import sys

import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--n_queens", type=int, default=8,
        help="The number of queens, which equals the height and the weight of a board")
args = parser.parse_args()


def is_valid(sol, r, c):
    for (i, j) in sol:
        if i == r:
            return False
        if j == c:
            return False
        if np.abs(r - i) == np.abs(c - j):
            return False
    return True


def n_queen(n):
    sol = []
    while len(sol) < n:
        row = len(sol)
        col = -1
        while True:
            col += 1
            if is_valid(sol, row, col):
                sol.append((row, col))
                break
            while (row == len(sol) and col >= n - 1):
                if len(sol) > 0:
                    row, col = sol.pop()
                else:
                    return []

    return(sol)


def main(argv):
    sol = n_queen(args.n_queens)
    print("n=%i, sol=%s" % (args.n_queens, str(sol)))


if __name__ == "__main__":
    main(sys.argv)
