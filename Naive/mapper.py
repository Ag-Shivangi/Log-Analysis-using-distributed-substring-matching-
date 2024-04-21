#!/usr/bin/env python3
"""mapper.py"""

import sys
pattern = "the"


def mapper():
    for line in sys.stdin:
        text, pattern, text_index, pattern_index = line.strip().split("\t")
        for i in range(len(text)):
            if text[i:i+len(pattern)] == pattern:
                print(f"{int(text_index) + i - int(pattern_index)}\t{pattern_index}")


if __name__ == "__main__":
    mapper()
