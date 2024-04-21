#!/usr/bin/env python

import sys
import os
from collections import defaultdict

# Implement Boyer-Moore Algorithm
class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.m = len(pattern)
        self.bad_char = defaultdict(int)
        self.preprocess_bad_char()

    def preprocess_bad_char(self):
        for i in range(self.m):
            self.bad_char[self.pattern[i]] = i

    def search(self, text):
        n = len(text)
        if n < self.m:
            return -1
        
        skip = 0
        while skip <= n - self.m:
            j = self.m - 1
            while j >= 0 and self.pattern[j] == text[skip + j]:
                j -= 1
            if j < 0:
                return skip
            else:
                skip += max(1, j - self.bad_char.get(text[skip + j], -1))
        return -1

# Mapper Function
def mapper():
    pattern = os.environ['PATTERN']
    boyer_moore = BoyerMoore(pattern)
    lineid = 0
    for line in sys.stdin:
        lineid += 1
        line = line.strip()
        offset = boyer_moore.search(line)
        if offset != -1:
            print(f"{offset}\t{lineid}")
            
if __name__ == "__main__":
    mapper()