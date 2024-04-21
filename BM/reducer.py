#!/usr/bin/env python

import sys

# Reducer Function
def reducer():
    # offset_counts = defaultdict(int)
    current_key = None
    current_matches = []
    for line in sys.stdin:
        line = line.strip()
        key, match = line.split("\t")
        if key != current_key:
            if current_key:
                print(f"{current_key}\t{current_matches}")
            current_key = key
            current_matches = [match]
        else:
            current_matches.append(match)
    if current_key:
        print(f"{current_key}\t{current_matches}")
    #     if key == "offset":
    #         offset = int(value)
    #         offset_counts[offset] += 1
    # # Process the offset_counts dictionary further if needed
    # for offset, count in offset_counts.items():
    #     print("offset: {}, count: {}".format(offset, count))

if __name__ == "__main__":
    reducer()
