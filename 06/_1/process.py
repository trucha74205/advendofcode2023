import time
import re
from functools import reduce

start_time = time.time()

file_path = "input.txt"
total_sum = 0


def getNumbersFromString(str):
    numbers = re.findall(r'\b\d+\b', line)
    return list(map(int, numbers))


def getDistanceForChargeTime(time, charge_time):
    if charge_time >= time:
        return 0
    return (time - charge_time) * charge_time


times = []
distances = []

with open(file_path, "r") as file:
    line = file.readline()
    times = getNumbersFromString(line)
    line = file.readline()
    distances = getNumbersFromString(line)

records = []

for index, t in enumerate(times):
    number_of_new_records = 0
    found_record = False
    for charge_time in range(1, t):
        distance = getDistanceForChargeTime(t, charge_time)
        if distance > distances[index]:
            number_of_new_records += 1
            found_record = True
        elif found_record:
            records.append(number_of_new_records)
            break

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Total sum of first and last digits: {reduce(lambda x, y: x * y, records)}")
