#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample usage:
python n-queens-closed-form.py -n 9
"""


import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--n_queens", type=int, default=8,
        help="The number of queens, which equals the height and the weight of a board")
args = parser.parse_args()


def n_queen(n):
    if n == 2 or n == 3:
        return []
    if n % 2 == 0 and (n - 2) % 6 != 0:
        sol_set1 = [(j, 2*j+1) for j in range(n//2)]
        sol_set2 = [(n//2+j, 2*j) for j in range(n//2)]
        return sol_set1 + sol_set2
    if n % 2 == 0 and n % 6 != 0:
        sol_set1 = [(j, (2*j + n//2 - 1) % n) for j in range(n//2)]
        sol_set2 = [(n-1-j, n-((2*j+n//2) % n)) for j in range(n//2)]
        return sol_set1 + sol_set2
    else:  # n is odd
        sol_set1 = [(j, 2*j+1) for j in range(n//2)]
        sol_set2 = [(n//2+j, 2*j) for j in range(n//2)]
        sol_set3 = [(n-1, n-1)]
        return sol_set1 + sol_set2 + sol_set3
        

def main(argv):
    sol = n_queen(args.n_queens)
    print("n=%i, sol=%s" % (args.n_queens, str(sol)))


if __name__ == "__main__":
    main(sys.argv)
