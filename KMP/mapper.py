#!/usr/bin/env python3
"""mapper.py"""
import sys
pattern="the"
def mapper():
    pattern_length = len(pattern)  
    for line_number, line in enumerate(sys.stdin):
        line = line.strip()
        # Send overlapping chunks of the text with indices
        for i in range(0, len(line), pattern_length - 1):
            if i + pattern_length < len(line):
                chunk = line[i:i + 2 * pattern_length - 1]  
            else:
                # The last chunk might be shorter
                chunk = line[i:]  
            print(f"{line_number}:{i}\t{chunk}")

if __name__ == "__main__":
    mapper()
