reader = open("./num_chunks.txt", "r")
_, num_pattern = reader.readline().strip().split("\t")

num_pattern = int(num_pattern)

reader.close()

reader = open("./tmp_output.txt", "r")

for line in reader.readlines():
    idx, sp = line.strip().split("\t")
    if int(sp) == num_pattern:
        print(idx)
