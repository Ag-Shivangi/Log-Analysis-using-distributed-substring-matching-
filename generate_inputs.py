import sys
import random

text_file_length = int(sys.argv[1])
pattern_file_length = int(sys.argv[2])

text_file_name = sys.argv[3]
pattern_file_name = sys.argv[4]

with open(pattern_file_name, "w") as f:
    for _ in range(pattern_file_length):
        f.write(random.choice(['a', 'b']))

with open(text_file_name, "w") as f:
    for _ in range(text_file_length):
        f.write(random.choice(['a', 'b']))
