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


def getNextKeys(current_keys, rl_instruction):
    next_keys = []
    for key in current_keys:
        next_keys.append(rlMap[key][rlInt[rl_instruction]])
    return next_keys


def finishReached(keys):
    for key in keys:
        if not key.endswith("Z"):
            return False
    return True


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

i = 0
rlLen = len(rlInstructions)

new_keys = list(filter(lambda x: x.endswith("A"), rlMap.keys()))


while not finishReached(new_keys):
    if i % 1000000 == 0:
        print(f"Step {'{:,}'.format(i).replace(',', '.')}")
    new_keys = getNextKeys(new_keys, rlInstructions[i % rlLen])
    i += 1

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Needed steps: {i}")
