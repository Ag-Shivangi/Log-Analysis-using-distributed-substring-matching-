#!/usr/bin/env python3
"""reducer.py"""

import sys

def rabin_karp_hash(s, base=256, prime=101):
    h = 0
    for char in s:
        h = (h * base + ord(char)) % prime
    return h

def reducer():
    pattern = 'the'  
    pattern_hash = rabin_karp_hash(pattern)

    for line in sys.stdin:
        key, value = line.strip().split('\t')
        substring_hash = rabin_karp_hash(value)

        if substring_hash == pattern_hash and value == pattern:
            print(f"Found '{pattern}' at position {key}")

if __name__ == "__main__":
    reducer()
