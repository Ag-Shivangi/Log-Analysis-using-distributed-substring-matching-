#!/usr/bin/env python3
"""mapper.py"""

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


def mapper():
    for line in sys.stdin:
        file_text, pattern_text, file_index, pattern_index = line.strip().split("\t")
        file_index = int(file_index)
        pattern_index = int(pattern_index)
        positions = KMP_search(pattern_text, file_text)
        for pos in positions:
            print(f"{file_index + pos - pattern_index}\t{pattern_index}")


if __name__ == "__main__":
    mapper()
