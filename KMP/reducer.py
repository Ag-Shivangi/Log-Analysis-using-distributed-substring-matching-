#!/usr/bin/env python3
"""reducer.py"""

import sys


def reducer():
    current_idx = None
    starting_pos = []
    for line in sys.stdin:
        k, v = line.strip().split("\t")
        if k == current_idx:
            starting_pos.append(int(v))
        else:
            if current_idx:
                print(f"{current_idx}\t{len(starting_pos)}")
            current_idx = k
            starting_pos = [int(v)]

    if current_idx:
        print(f"{current_idx}\t{len(starting_pos)}")


if __name__ == "__main__":
    reducer()
