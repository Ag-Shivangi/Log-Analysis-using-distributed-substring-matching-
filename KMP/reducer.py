#!/usr/bin/env python3
"""reducer.py"""

import sys

def KMP_search(pattern, text):
    # Build the partial match (pi) table 
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    # Perform search
    j = 0
    results = []
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                results.append(i - j)
                j = pi[j]
            else:
                j += 1
    return results

def reducer():
    pattern = 'the'  
    for line in sys.stdin:
        key, value = line.strip().split('\t')
        line_number, start_pos = map(int, key.split(':'))
        positions = KMP_search(pattern, value)

        for pos in positions:
            print(f"Found '{pattern}' at line {line_number} position {start_pos + pos}")

if __name__ == "__main__":
    reducer()
