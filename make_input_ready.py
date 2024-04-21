import sys

ss_chunk_size = int(sys.argv[1])
ss_file_name = sys.argv[2]
pattern_chunk_size = int(sys.argv[3])
pattern_file_name = sys.argv[4]
output_file_name = sys.argv[5]

ss_reader = open(ss_file_name, "r")

output_writer = open(output_file_name, "w")


ss_idx = 0
ss_prefix = ""

num_ss = 0
num_pattern = 0

while True:
    ss_chunk = ss_reader.read(ss_chunk_size).strip()
    if not ss_chunk:
        break
    pattern_reader = open(pattern_file_name, "r")
    pattern_idx = 0
    while True:
        pattern_chunk = pattern_reader.read(pattern_chunk_size).strip()
        if not pattern_chunk:
            break
        output_writer.write(
            f"{ss_prefix + ss_chunk}\t{pattern_chunk}\t{ss_idx}\t{pattern_idx}\n")
        pattern_idx += pattern_chunk_size
        if num_ss == 0:
            num_pattern += 1
    pattern_reader.close()
    ss_prefix = ss_chunk[-pattern_chunk_size + 1:]
    ss_idx += ss_chunk_size + - \
        (pattern_chunk_size - 1 if ss_idx == 0 else 0)
    num_ss += 1

writer = open("num_chunks.txt", "w")
writer.write(f"{num_ss}\t{num_pattern}")
writer.close()
