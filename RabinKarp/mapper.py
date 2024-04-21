#!/usr/bin/env python3
"""mapper.py"""

import sys
pattern='the'
def mapper():
    pattern_length = len(pattern)  

    for line_number, line in enumerate(sys.stdin):
        line = line.strip()
        for i in range(len(line) - pattern_length + 1):
            # Emit the position and the substring at that position
            print(f"{i}\t{line[i:i + pattern_length]}")

if __name__ == "__main__":
    mapper()
