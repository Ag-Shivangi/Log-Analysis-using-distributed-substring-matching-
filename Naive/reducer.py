#!/usr/bin/env python3
"""reducer.py"""

import sys

def brute_force_search(pattern, text):
    m, n = len(pattern), len(text)
    results = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            results.append(i)
    return results

def reducer():
    pattern = 'the'
    for line in sys.stdin:
        line_number, text = line.strip().split('\t')
        matches = brute_force_search(pattern, text)
        for match in matches:
            print(f"Found '{pattern}' at line {line_number} position {match}")

if __name__ == "__main__":
    reducer()
