#!/usr/bin/env python3
"""mapper.py"""

import sys
pattern="the"

def mapper():
    for line_number, line in enumerate(sys.stdin):
        line = line.strip()
        print(f"{line_number}\t{line}")

if __name__ == "__main__":
    mapper()
