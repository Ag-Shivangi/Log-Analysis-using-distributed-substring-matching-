#!/usr/bin/env python

import sys

def main():
    current_key = None
    current_matches = []
    for line in sys.stdin:
        key, match = line.strip().split("\t")
        if key != current_key:
            if current_key:
                print(f"{current_key}\t{current_matches}")
            current_key = key
            current_matches = [match]
        else:
            current_matches.append(match)
    if current_key:
        print(f"{current_key}\t{current_matches}")

if __name__ == "__main__":
    main()
