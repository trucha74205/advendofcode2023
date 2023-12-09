import time
import re
import math

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


def nextIteration(new_keys):
    solutions = [0] * len(new_keys)
    for nkIndex, new_key in enumerate(new_keys):
        i = 0
        while new_key[-1] != "Z":
            rl_index = rlInt[rlInstructions[i % rlLen]]
            new_key = rlMap[new_key][rl_index]
            i += 1
        solutions[nkIndex] = i
    return solutions


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
new_keys = list(filter(lambda x: x.endswith("A"), rlMap.keys()))
solutions = [0] * len(new_keys)
rlLen = len(rlInstructions)

for nkIndex, new_key in enumerate(new_keys):
    i = 0
    while new_key[-1] != "Z":
        rl_index = rlInt[rlInstructions[i % rlLen]]
        new_key = rlMap[new_key][rl_index]
        i += 1
    solutions[nkIndex] = i

print(f"Solutions: {solutions}")
print(f"LCM: {math.lcm(*solutions)}")
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Needed steps: {i}")
