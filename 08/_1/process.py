import time
import re

start_time = time.time()

file_path = "input.txt"
total_sum = 0

rlMap = {}

rlInstructions = []

rlInt = {
    "R": 1,
    "L": 0
}

# Define the pattern for matching 3-character strings
pattern = re.compile(r'\b\w{3}\b')

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if len(rlInstructions) == 0:
            rlInstructions = list(line)
            continue
        elif line == "":
            continue

        matches = pattern.findall(line)

        rlMap[matches[0]] = matches[1:]

new_key = "AAA"
i = 0
rlLen = len(rlInstructions)

while new_key != "ZZZ":
    rl_index = rlInt[rlInstructions[i % rlLen]]
    new_key = rlMap[new_key][rl_index]
    i += 1

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Needed steps: {i}")
