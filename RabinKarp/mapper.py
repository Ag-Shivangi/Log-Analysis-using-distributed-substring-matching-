#!/usr/bin/env python3
"""mapper.py"""

import random
import sys

d = 10


def search(pattern: str, text: str, q: int) -> list[int]:
    m = len(pattern)
    n = len(text)
    p = t = i = j = 0
    h = 1
    matches = []
    for i in range(m-1):
        h = (h*d) % q
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                matches.append(i)
        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
            if t < 0:
                t = t+q
    return matches


def mapper() -> None:
    q = 131
    for line in sys.stdin:
        text, pattern, text_index, pattern_index = line.strip().split()
        text_index = int(text_index)
        pattern_index = int(pattern_index)
        matches = search(pattern, text, q)
        for match in matches:
            print(f"{text_index + match - pattern_index}\t{pattern_index}")


if __name__ == "__main__":
    mapper()
